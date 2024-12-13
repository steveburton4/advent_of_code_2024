from multiprocessing import Process, Manager
import os
from copy import deepcopy

def read_input(file_name):
    rows = []

    with open(file_name, 'r') as file:
        for line in (item for item in file if item.strip()):
            rows.append(list(line.strip()))

    return rows

def find_start_point(rows):
    for row_count in range(0,len(rows)):
        for character_count in range(0,len(rows[row_count])):
            if rows[row_count][character_count] == '^':
                return row_count, character_count
    
    raise Exception("No start point found")

def get_next_check_point(current_point, current_direction):
    match current_direction:
        case '<':
            return int(current_point[0]), int(current_point[1])-1
        case '>':
            return int(current_point[0]), int(current_point[1])+1
        case '^':
            return int(current_point[0])-1, int(current_point[1])
        case 'v':
            return int(current_point[0])+1, int(current_point[1])
        case _:
            raise Exception('Invalid direction')

def get_next_direction(current_direction):
    match current_direction:
        case '<':
            return '^'
        case '>':
            return 'v'
        case '^':
            return '>'
        case 'v':
            return '<'
        case _:
            raise Exception('Invalid direction')

def is_map_full(mapped_rows):
    for mapped_row in mapped_rows:
        for mapped_location in mapped_row:
            if mapped_location == ".":
                return False
    
    return True

def is_loop_created(next_point, direction, areas_patrolled):
    return (next_point, direction) in areas_patrolled

def can_continue_mapping(next_point, direction, areas_patrolled, mapped_rows):
    if next_point[0] < 0 or next_point[1] < 0:
        return False, False
    
    if next_point[0] >= len(mapped_rows) or next_point[1] >= len(mapped_rows[next_point[0]]):
        return False, False
    
    if is_loop_created(next_point, direction, areas_patrolled):
        return False, True

    if is_map_full(mapped_rows):
        return False, False

    return True, False

def map_route(start_direction, start_point, rows):
    areas_patrolled = []
    mapped_rows = deepcopy(rows)
    mapped_rows[start_point[0]][start_point[1]] = 'X'
    direction = start_direction
    current_point = start_point
    areas_patrolled.append((start_point,direction))
    next_point = get_next_check_point(start_point, start_direction)
    can_continue = can_continue_mapping(next_point, start_direction, areas_patrolled, mapped_rows)

    while (can_continue[0]):
        if mapped_rows[next_point[0]][next_point[1]] == '#':
            direction = get_next_direction(direction)
            next_point = get_next_check_point(current_point, direction)
        else:
            mapped_rows[next_point[0]][next_point[1]] = 'X'
            areas_patrolled.append((next_point,direction))
            current_point = next_point
            next_point = get_next_check_point(next_point, direction)

        can_continue = can_continue_mapping(next_point, direction, areas_patrolled, mapped_rows)

    return mapped_rows, can_continue[1]

def count_infinite_loops_for_row(rows, row_count, start_point, start_direction, loops_found, lock_loops, rows_checked, lock_rows):
    print("CHECKING ROW: " + str(row_count))
    for character_count in range(0,len(rows[row_count])):
        if rows[row_count][character_count] == '.':
            check_map = deepcopy(rows)
            check_map[row_count][character_count] = "#"
            if map_route(start_direction, start_point, check_map)[1]:
                with lock_loops:
                    loops_found.value += 1
    
    with lock_rows:
        rows_checked.value += 1

    print("ROWS CHECKED: " + str(rows_checked.value) + ", LOOPS FOUND: " + str(loops_found.value))

    return loops_found.value

def count_infinite_loops_threaded(start_direction, start_point, rows):     
    with Manager() as manager:
        loops_found = manager.Value('loops_found', 0)
        rows_checked = manager.Value('rows_checked', 0)
        lock_l = manager.Lock()
        lock_r = manager.Lock()
        num_processes = os.cpu_count()
        rows_checked_count = 0

        while rows_checked_count < len(rows):
            processes = []
            for _ in range(0, num_processes):
                if rows_checked_count < len(rows):
                    process = Process(target=count_infinite_loops_for_row, args=(rows, rows_checked_count, start_point, start_direction, loops_found, lock_l, rows_checked, lock_r))
                    processes.append(process)
                    rows_checked_count += 1

            for process in processes:
                process.start()

            for process in processes:
                process.join()

        return loops_found.value

def count_travelled_route(mapped_route):
    spaces_hit = 0
    for row in mapped_route:
        for character in row:
            if character == 'X':
                spaces_hit += 1
    
    return spaces_hit

if __name__ == '__main__':
    input = read_input('Day 6/input.txt')
    start_point = find_start_point(input)
    mapped_rows =  map_route('^', start_point, input)
    count_of_route = count_travelled_route(mapped_rows[0])
    loops_found_count = count_infinite_loops_threaded('^', start_point, input)

    print('Day 6 total of patrolled spaces is: ' + str(count_of_route))
    print('Day 6 total of loops is: ' + str(loops_found_count))
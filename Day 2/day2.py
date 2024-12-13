import csv

def read_inputs(file_name):
    rows = []

    with open(file_name, newline='\n') as file:
        file_reader = csv.reader(file, delimiter=' ')
        for row in file_reader:
            row_list = []
            for column in row:
                row_list.append(int(column))
            rows.append(row_list)
    
    return rows

def is_safe_difference_between_two_numbers(previous_number, current_number):
    diff = abs(previous_number - current_number)
    return not (diff < 1 or diff > 3)

def is_list_safe(unsorted_number_list):
    if not unsorted_number_list:
        return False
    
    previous_number = unsorted_number_list[0]
    previous_number_was_increasing = True
    
    for current_item_count in range(1, len(unsorted_number_list)):
        current_item = unsorted_number_list[current_item_count]
        if not is_safe_difference_between_two_numbers(previous_number, current_item):
            return False
        
        is_current_number_increasing = (previous_number < current_item)
        if current_item_count > 1 and previous_number_was_increasing is not is_current_number_increasing:
            return False

        previous_number_was_increasing = is_current_number_increasing
        previous_number = current_item
    
    return True

def is_list_safe_allowing_an_error(number_list):
    if is_list_safe(number_list):
        return True

    for list_item_count in range(0, len(number_list)):
        check_list = number_list.copy()
        del(check_list[list_item_count])
        if is_list_safe(check_list):
            return True
        
    return False

def count_safe_rows(rows, allow_error):
    safe_count = 0
    for row in rows:
        is_safe_row = is_list_safe_allowing_an_error(row) if allow_error else is_list_safe(row)
        if is_safe_row:
            safe_count += 1

    return safe_count

if __name__ == '__main__':
    input_rows = read_inputs('Day 2/input.csv')
    print('Day 2 safe row count is: ' + str(count_safe_rows(input_rows, False)))
    print('Day 2 safe row count with a skip is: ' + str(count_safe_rows(input_rows, True)))

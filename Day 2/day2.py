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
    return not (diff == 0 or diff > 3)

def is_list_safe(unsorted_number_list):
    if not unsorted_number_list:
        return False
    
    previous_number = int(unsorted_number_list[0])
    previous_number_was_increasing = True
    
    for current_item in range(1, len(unsorted_number_list)):
        current_number = int(unsorted_number_list[current_item])
        if not is_safe_difference_between_two_numbers(previous_number, current_number):
            return False
        
        is_current_number_increasing = (previous_number < current_number)
        if current_item > 1 and previous_number_was_increasing is not is_current_number_increasing:
            return False

        previous_number_was_increasing = is_current_number_increasing
        previous_number = current_number
    
    return True

def count_safe_rows(rows):
    safe_count = 0
    for row in rows:
        if is_list_safe(row):
            safe_count += 1
    
    return safe_count

input_rows = read_inputs('Day 2/input.csv')
safe_row_count = count_safe_rows(input_rows)
print('Day 2 safe row count is: ' + str(safe_row_count))
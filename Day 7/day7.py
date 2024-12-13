from functools import reduce
from operator import add, mul
import itertools

def read_input(file_name):
    rows = []

    with open(file_name, 'r') as file:
        for line in file:
            split_line = line.split(':')
            operators = split_line[1].strip().split()
            rows.append((int(split_line[0].strip()), list(int(operator.strip()) for operator in operators)))

    return rows

def do_operators_meet_total_in_product(total, operators, allow_concatenation):
    concatenate_numbers = lambda x,y: int(str(x) + str(y))
    method_set = (add,mul,concatenate_numbers) if allow_concatenation else (add,mul)

    all_possible_totals = [operators[0]]
    for operator in operators[1:]:
        all_possible_totals = [
            operator_method(possible_total,operator) \
            for possible_total in all_possible_totals \
            for operator_method in method_set
        ]

    return total in all_possible_totals

def get_valid_rows(rows, allow_concatenation):
    return [
        row for row in rows
        if do_operators_meet_total_in_product(row[0], row[1], allow_concatenation)
    ]

if __name__ == '__main__':
    input = read_input('Day 7/input.txt')
    valid_rows = get_valid_rows(input, False)
    total = sum(valid_row[0] for valid_row in valid_rows)
    valid_rows_with_concatenation = get_valid_rows(input, True)
    total_with_concatenation = sum(valid_row_with_concatenation[0] for valid_row_with_concatenation in valid_rows_with_concatenation)
    print('Day 7 total calibration result is: ' + str(total))
    print('Day 7 total calibration result with concatenation allowed is: ' + str(total_with_concatenation))
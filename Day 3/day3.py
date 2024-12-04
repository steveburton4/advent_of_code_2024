import re

def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def find_valid_mul_statements(input_text):
    regex_for_mul = 'mul\(\d{1,3},\d{1,3}\)'
    return re.findall(regex_for_mul, input_text)

def get_total_of_single_mul_statement(mul_statement_text):
    mul_statement_text = mul_statement_text.replace('mul(', '').replace(')', '')
    mul_statement_number_list = mul_statement_text.split(',')
    return int(mul_statement_number_list[0]) * int(mul_statement_number_list[1])

def get_total_of_mul_statements(list_of_statements_text):
    total = 0
    for mul_statement in list_of_statements_text:
        total += get_total_of_single_mul_statement(mul_statement)
    return total

mul_statement_full_text = read_input('Day 3/input.txt')
mul_statement_list = find_valid_mul_statements(mul_statement_full_text)
mul_statement_total = get_total_of_mul_statements(mul_statement_list)
print('Day 3 total of mul statements is: ' + str(mul_statement_total))
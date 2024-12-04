import re

def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read()
    
def find_all_enabled_sections(input_text):
    enabled_sections = []
    regex_text = "(?=(do\(\)|don't\(\)))"
    for section in re.split(regex_text, input_text):
        if section and section != 'do()' and section != "don't()":
            if section.startswith('do()'):
                enabled_sections.append(section.removeprefix('do()'))
            elif not section.startswith("don't()"):
                enabled_sections.append(section)
    
    return enabled_sections

def find_valid_mul_statements(input_text):
    regex_for_mul = 'mul\(\d{1,3},\d{1,3}\)'
    return re.findall(regex_for_mul, input_text)

def find_valid_mul_statements_from_list_text(mul_statements_text_list):
    valid_mul_statements = []
    for mul_statement_text in mul_statements_text_list:
        valid_mul_statements.extend(find_valid_mul_statements(mul_statement_text))

    return valid_mul_statements

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

mul_enabled_sections = find_all_enabled_sections(mul_statement_full_text)
mul_statement_list = find_valid_mul_statements_from_list_text(mul_enabled_sections)
mul_enabled_statement_total = get_total_of_mul_statements(mul_statement_list)
print('Day 3 total of enabled mul statements is: ' + str(mul_enabled_statement_total))

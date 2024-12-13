import re

def read_input(file_name):
    with open(file_name, 'r') as file:
        return [line.rstrip() for line in file]

def find_xmas_instances_horizontal(lines_to_check):
    total_instances_horizontal = 0
    for line_to_check in lines_to_check:
        total_instances_horizontal += len(re.findall('XMAS',line_to_check))
        total_instances_horizontal += len(re.findall('SAMX',line_to_check))

    return total_instances_horizontal

def find_xmas_instances_vertical(lines_to_check):
    total_instances_vertical = 0
    for line_number in range(0, len(lines_to_check)):
        for character_number in range(0, len(lines_to_check[line_number])):
            if len(lines_to_check) > (line_number + 3):
                check_string = lines_to_check[line_number][character_number] \
                + lines_to_check[line_number + 1][character_number] \
                + lines_to_check[line_number + 2][character_number] \
                + lines_to_check[line_number + 3][character_number]

                if "XMAS" == check_string or "SAMX" == check_string:
                    total_instances_vertical += 1

    return total_instances_vertical

def is_check_string_diagonal(lines_to_check, l_start, c_start, check_lines_forward, check_characters_forward):
    check_string = ''
    for count in range(0, 4):
        line_number_to_check = l_start + count if check_lines_forward else l_start - count
        character_number_to_check = c_start + count if check_characters_forward else c_start - count
        check_string += lines_to_check[line_number_to_check][character_number_to_check]

    return "XMAS" == check_string

def find_xmas_instances_diagonal(lines_to_check):
    total_instances_diagonal = 0
    for line_number in range(0, len(lines_to_check)):
        for character_number in range(0, len(lines_to_check[line_number])):
            if lines_to_check[line_number][character_number] == 'X':
                if (len(lines_to_check) > (line_number + 3)) and (len(lines_to_check[line_number]) > (character_number + 3)):
                    if is_check_string_diagonal(lines_to_check, line_number, character_number, True, True):
                        total_instances_diagonal += 1
                

                if (len(lines_to_check) > (line_number + 3)) and ((character_number - 3) >= 0):
                    if is_check_string_diagonal(lines_to_check, line_number, character_number, True, False):
                        total_instances_diagonal += 1
                

                if (line_number - 3) >= 0 and (len(lines_to_check[line_number]) > (character_number + 3)):
                    if is_check_string_diagonal(lines_to_check, line_number, character_number, False, True):
                        total_instances_diagonal += 1
                

                if (line_number - 3) >= 0 and ((character_number - 3) >= 0):
                    if is_check_string_diagonal(lines_to_check, line_number, character_number, False, False):
                        total_instances_diagonal += 1

    return total_instances_diagonal

def find_x_mas_instances(lines_to_check):
    total_x_mas_instances = 0
    for line_number in range(1, len(lines_to_check)):
        for character_number in range(1, len(lines_to_check[line_number])):
            if lines_to_check[line_number][character_number] == 'A':
                if (len(lines_to_check) > (line_number + 1) and len(lines_to_check[line_number]) > (character_number + 1)):
                    check_string = ''.join([lines_to_check[line_number-1][character_number-1], \
                        lines_to_check[line_number][character_number], \
                        lines_to_check[line_number+1][character_number+1]])

                    check_string_two = ''.join([lines_to_check[line_number-1][character_number+1], \
                        lines_to_check[line_number][character_number], \
                        lines_to_check[line_number+1][character_number-1]])
                    
                    if (("MAS" == check_string or "SAM" == check_string) and \
                        ("MAS" == check_string_two or "SAM" == check_string_two)):
                        total_x_mas_instances += 1

    return total_x_mas_instances

def find_xmas_instances(lines_to_check):
    return find_xmas_instances_horizontal(lines_to_check) + \
           find_xmas_instances_vertical(lines_to_check) + \
           find_xmas_instances_diagonal(lines_to_check)

if __name__ == '__main__':
    input_lines = read_input('Day 4/input.txt')
    total_instances = find_xmas_instances(input_lines)
    print('Day 4 total of xmas instances is: ' + str(total_instances))

    total_instances_x_mas = find_x_mas_instances(input_lines)
    print('Day 4 total of x-mas instances is: ' + str(total_instances_x_mas))

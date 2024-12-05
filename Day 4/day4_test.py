from day4 import read_input, find_xmas_instances_horizontal, find_xmas_instances_vertical
from day4 import find_xmas_instances_diagonal, is_check_string_diagonal, find_xmas_instances
from day4 import find_x_mas_instances

def test_day_4_read_valid_input():
    expected = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM','MSAMASMSMX','XMASAMXAMM','XXAMMXXAMA','SMSMSMSXSS','SAXAAASAAA','MAMSMXMMMM','MXMXAXMASX']
    actual = read_input('Day 4/test_input.txt')
    assert expected == actual

def test_day_4_find_xmas_instances_horizontal():
    input_lines = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM','MSAMASMSMX','XMASAMXAMM','XXAMMXXAMA','SMSMSMSXSS','SAXAAASAAA','MAMSMXMMMM','MXMXAXMASX']
    expected = 5
    actual = find_xmas_instances_horizontal(input_lines)
    assert expected == actual

def test_day_4_find_xmas_instances_vertical():
    input_lines = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM','MSAMASMSMX','XMASAMXAMM','XXAMMXXAMA','SMSMSMSXSS','SAXAAASAAA','MAMSMXMMMM','MXMXAXMASX']
    expected = 3
    actual = find_xmas_instances_vertical(input_lines)
    assert expected == actual

def test_day_4_find_xmas_instances_diagonal():
    input_lines = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM','MSAMASMSMX','XMASAMXAMM','XXAMMXXAMA','SMSMSMSXSS','SAXAAASAAA','MAMSMXMMMM','MXMXAXMASX']
    expected = 11
    actual = find_xmas_instances_diagonal(input_lines)
    assert expected == actual

def test_day_4_is_check_string_diagonal():
    input_lines = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM','MSAMASMSMX','XMASAMXAMM','XXAMMXXAMA','SMSMSMSXSS','SAXAAASAAA','MAMSMXMMMM','MXMXAXMASX']
    assert is_check_string_diagonal(input_lines, 3, 9, True, False)

def test_day_4_is_check_string_diagonal_invalid():
    input_lines = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM','MSAMASMSMX','XMASAMXAMM','XXAMMXXAMA','SMSMSMSXSS','SAXAAASAAA','MAMSMXMMMM','MXMXAXMASX']
    assert not is_check_string_diagonal(input_lines, 2, 9, True, False)
    
def test_day_4_find_xmas_instances():
    input_lines = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM','MSAMASMSMX','XMASAMXAMM','XXAMMXXAMA','SMSMSMSXSS','SAXAAASAAA','MAMSMXMMMM','MXMXAXMASX']
    expected = 19
    actual = find_xmas_instances(input_lines)
    assert expected == actual
    
def test_day_4_find_x_mas_instances():
    input_lines = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM','MSAMASMSMX','XMASAMXAMM','XXAMMXXAMA','SMSMSMSXSS','SAXAAASAAA','MAMSMXMMMM','MXMXAXMASX']
    expected = 9
    actual = find_x_mas_instances(input_lines)
    assert expected == actual

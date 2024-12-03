from day2 import read_inputs, is_safe_difference_between_two_numbers, is_list_safe, count_safe_rows

def test_day_2_read_valid_input():
    expected_lists = [[1,5,8],[2,5,100,4,5]]
    lists = read_inputs('Day 2/test_input.csv')
    assert expected_lists == lists

def test_day_2_is_safe_difference_between_two_numbers():
    assert is_safe_difference_between_two_numbers(1, 2)

def test_day_2_is_safe_difference_between_two_numbers_reverse_input():
    assert is_safe_difference_between_two_numbers(2, 1)

def test_day_2_is_safe_difference_between_two_numbers_three_apart():
    assert is_safe_difference_between_two_numbers(1, 4)

def test_day_2_is_safe_difference_between_two_numbers_three_apart_reverse_input():
    assert is_safe_difference_between_two_numbers(4, 1)

def test_day_2_is_unsafe_difference_between_two_numbers_the_same():
    assert not is_safe_difference_between_two_numbers(2, 2)

def test_day_2_is_unsafe_difference_between_two_numbers_greater_than_three():
    assert not is_safe_difference_between_two_numbers(6, 2)

def test_day_2_is_unsafe_difference_between_two_numbers_greater_than_three_reverse_input():
    assert not is_safe_difference_between_two_numbers(2, 6)

def test_day_2_is_safe_list_increasing():
    input_list = [3,5,8]
    assert is_list_safe(input_list)

def test_day_2_is_safe_list_decreasing():
    input_list = [10,7,6]
    assert is_list_safe(input_list)

def test_day_2_is_unsafe_list_not_all_increasing_or_decreasing():
    input_list = [3,3,4]
    assert not is_list_safe(input_list)

def test_day_2_is_unsafe_list_differ_by_more_than_three_increasing():
    input_list = [3,5,9]
    assert not is_list_safe(input_list)

def test_day_2_is_unsafe_list_differ_by_more_than_three_decreasing():
    input_list = [10,6,3]
    assert not is_list_safe(input_list)

def test_day_2_is_unsafe_increasing_and_decreasing():
    input_list = [8,6,3,2,5,6]
    assert not is_list_safe(input_list)

def test_day_2_count_safe_rows():
    input_lists = [[10,7,6],[3,5,8,9],[10,6,3]]
    expected = 2
    actual = count_safe_rows(input_lists)
    assert expected == actual

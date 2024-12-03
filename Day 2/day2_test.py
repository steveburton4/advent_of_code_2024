from day2 import read_inputs, is_safe_difference_between_two_numbers, is_list_safe, is_list_safe_allowing_an_error, count_safe_rows

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

def test_day_2_is_safe_list_with_one_allowed_skip_increasing():
    input_list = [3,5,4,8]
    assert is_list_safe_allowing_an_error(input_list)

def test_day_2_is_safe_list_with_one_allowed_skip_at_start_increasing():
    input_list = [6,5,7,8]
    assert is_list_safe_allowing_an_error(input_list)

def test_day_2_is_safe_list_with_one_allowed_skip_at_end_increasing():
    input_list = [3,5,8,6]
    assert is_list_safe_allowing_an_error(input_list)

def test_day_2_is_safe_list_with_one_allowed_skip_decreasing():
    input_list = [10,9,7,8,5,4]
    assert is_list_safe_allowing_an_error(input_list)

def test_day_2_is_safe_list_with_one_allowed_skip_big_diff_decreasing():
    input_list = [14,9,7,6,5,4]
    assert is_list_safe_allowing_an_error(input_list)

def test_day_2_is_safe_list_with_one_allowed_skip_big_diff_increasing():
    input_list = [1,9,4,5,8,10]
    assert is_list_safe_allowing_an_error(input_list)

def test_day_2_is_safe_list_with_one_allowed_skip_at_start_decreasing():
    input_list = [8,9,7,6,5,4]
    assert is_list_safe_allowing_an_error(input_list)

def test_day_2_is_safe_list_with_one_allowed_skip_at_end_decreasing():
    input_list = [10,9,7,6,5,5]
    assert is_list_safe_allowing_an_error(input_list)

def test_day_2_is_safe_list_with_one_allowed_skip_duplicate_numbers():
    input_list = [9,8,7,8,5,4]
    assert is_list_safe_allowing_an_error(input_list)

def test_day_2_is_unsafe_list_with_two_skips_increasing():
    input_list = [9,10,8,7,6,7,4]
    assert not is_list_safe_allowing_an_error(input_list)

def test_day_2_is_unsafe_list_with_two_skips_decreasing():
    input_list = [9,8,11,14,15,14,16]
    assert not is_list_safe_allowing_an_error(input_list)

def test_day_2_is_unsafe_list_with_two_big_diffs_increasing():
    input_list = [9,10,11,17,18,22,24]
    assert not is_list_safe_allowing_an_error(input_list)

def test_day_2_is_unsafe_list_with_two_big_diffs_decreasing():
    input_list = [91,87,85,84,80,76,75]
    assert not is_list_safe_allowing_an_error(input_list)

def test_day_2_count_safe_rows():
    input_lists = [[10,7,6],[3,5,8,9],[10,6,3]]
    expected = 2
    actual = count_safe_rows(input_lists, False)
    assert expected == actual

def test_day_2_count_safe_rows_allowing_an_error():
    input_lists = [[10,7,6],[3,5,8,9],[10,6,3]]
    expected = 3
    actual = count_safe_rows(input_lists, True)
    assert expected == actual

def test_day_2_count_safe_rows_allowing_an_error_large_list():
    input_lists = [[59,61,60,63,61,59,60],[96,94,91,89,87],[73,74,76,77,80,81],[5,6,7,10,12,14,15],[15,18,21,24,25,27,30,31],[36,39,41,44,47,48,50,51],[3,5,8,9],[10,6,3]]
    expected = 7
    actual = count_safe_rows(input_lists, True)
    assert expected == actual

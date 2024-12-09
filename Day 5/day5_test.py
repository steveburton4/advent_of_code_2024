from day5 import read_input, is_valid_update, do_ordering_rules_exist, get_valid_and_invalid_updates_lists
from day5 import get_middle_page, get_value_of_middle_pages, fix_invalid_update, fix_invalid_updates
import pytest

def test_day_5_read_valid_input():
    expected = ([[56,79],[16,95],[95,77],[11,19]], [[56,79,19,11], [16,95,77,65], [16,95,77]])
    actual = read_input('Day 5/test_input.txt')
    assert expected == actual

def test_day_5_do_ordering_rules_exist_valid():
    page_ordering_rules_lists = [[56,79],[16,95],[95,77],[11,19],[56,19],[56,11]]
    subsequent_pages_as_list = [79,19,11]
    actual = do_ordering_rules_exist(56, subsequent_pages_as_list, page_ordering_rules_lists)
    assert actual

def test_day_5_do_ordering_rules_exist_invalid():
    page_ordering_rules_lists = [[56,79],[16,95],[95,77],[11,19],[56,19]]
    subsequent_pages_as_list = [79,19,11]
    actual = do_ordering_rules_exist(56, subsequent_pages_as_list, page_ordering_rules_lists)
    assert not actual

def test_day_5_is_valid_update_valid():
    page_ordering_rules_lists = [[56,79],[16,95],[95,77],[19,11],[56,19],[79,11],[79,19],[56,11]]
    input_list = [56,79,19,11]
    actual = is_valid_update(input_list, page_ordering_rules_lists)
    assert actual

def test_day_5_is_valid_update_invalid():
    page_ordering_rules_lists = [[56,79],[16,95],[95,77],[11,19],[56,19]]
    input_list = [56,79,19,11]
    actual = is_valid_update(input_list, page_ordering_rules_lists)
    assert not actual

def test_day_5_is_valid_update_count():
    page_ordering_rules_lists = [[56,79],[16,95],[95,77],[19,11],[56,19],[79,11],[79,19],[56,11]]
    input_list = [[56,79,19,11], [16,95,77,65], [16,95,77]]
    expected = ([[56,79,19,11]],[[16,95,77,65], [16,95,77]])
    actual = get_valid_and_invalid_updates_lists(input_list, page_ordering_rules_lists)
    assert expected == actual

def test_day_5_get_middle_page_odd():
    expected = 19
    actual = get_middle_page([56,79,19,11,12])
    assert expected == actual

def test_day_5_get_middle_page_even():
    with pytest.raises(Exception) as e_info:
        get_middle_page([56,79,11,12])
        assert e_info.value == "Not even"

def test_day_5_get_value_of_middle_pages():
    expected = 37
    actual = get_value_of_middle_pages([[56,79,10,11,12],[56,79,19,11,12],[56,79,8,11,12]])
    assert expected == actual

def test_day_5_fix_invalid_update():
    page_ordering_rules_lists = [[95,16],[95,77],[95,65],[65,16],[65,77],[77,16],[56,11]]
    input_list = [16,95,77,65]
    expected = [95,65,77,16]
    actual = fix_invalid_update(input_list, page_ordering_rules_lists)
    assert expected == actual

def test_day_5_is_fix_invalid_updates():
    page_ordering_rules_lists = [[95,16],[95,77],[95,65],[65,16],[65,77],[77,16],[56,11]]
    input_lists = [[16,95,77,65], [16,95,77]]
    expected = [[95,65,77,16], [95,77,16]]
    actual = fix_invalid_updates(input_lists, page_ordering_rules_lists)
    assert expected == actual

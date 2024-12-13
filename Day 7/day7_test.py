from day7 import read_input, get_valid_rows, do_operators_meet_total_in_product
import pytest

def test_day_7_read_valid_input():
    expected = [
        (190,[10,19]),
        (3267,[81,40,27]),
        (83,[17,5]),
        (156,[15,6]),
        (7290,[6,8,6,15]),
        (161011,[16,10,13]),
        (192,[17,8,14]),
        (21037,[9,7,18,13]),
        (292,[11,6,16,20])
    ]
    actual = read_input('Day 7/test_input.txt')
    assert expected == actual

def test_day_7_do_operators_meet_total_in_product_valid():
    expected = True
    actual = do_operators_meet_total_in_product(195, [10, 19, 5], False)
    assert expected == actual

def test_day_7_do_operators_meet_total_in_product_invalid():
    expected = False
    actual = do_operators_meet_total_in_product(195, [10, 19, 6], False)
    assert expected == actual

def test_day_7_get_valid_rows_no_concatenation():
    input_rows = [
        (196,[10,19,6]),
        (3267,[81,40,27]),
        (83,[17,5]),
        (156,[15,6]),
        (7290,[6,8,6,15]),
        (161011,[16,10,13]),
        (192,[17,8,14]),
        (21037,[9,7,18,13]),
        (292,[11,6,16,20])
    ]
    expected = [
        (196,[10,19,6]),
        (3267,[81,40,27]),
        (292,[11,6,16,20])
    ]
    actual = get_valid_rows(input_rows, False)
    assert expected == actual

def test_day_7_get_valid_rows_with_concatenation():
    input_rows = [
        (196,[10,19,6]),
        (3267,[81,40,27]),
        (83,[17,5]),
        (156,[15,6]),
        (7290,[6,8,6,15]),
        (161011,[16,10,13]),
        (192,[17,8,14]),
        (21037,[9,7,18,13]),
        (292,[11,6,16,20])
    ]
    expected = [
        (196,[10,19,6]),
        (3267,[81,40,27]),
        (156,[15,6]),
        (7290,[6,8,6,15]),
        (192,[17,8,14]),
        (292,[11,6,16,20])
    ]
    actual = get_valid_rows(input_rows, True)
    assert expected == actual

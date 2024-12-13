from day6 import read_input, find_start_point, get_next_check_point, get_next_direction, map_route, count_travelled_route
from day6 import count_infinite_loops_for_row, count_infinite_loops_threaded
from multiprocessing import Process, Manager
import pytest

def test_day_6_read_valid_input():
    expected = [['.','.','.','.','.','.','#','.','.','.','.','#','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.'],
                ['.','.','.','#','.','.','^','.','.','.','.','.','.','.','#','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','#','.','.','.'],
                ['.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','#','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.']]
    actual = read_input('Day 6/test_input.txt')
    assert expected == actual

def test_day_6_find_start_point():
    input_rows = [['.','.','.','.','.','.','#','.','.','.','.','#','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.'],
                ['.','.','.','#','.','.','^','.','.','.','.','.','.','.','#','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','#','.','.','.'],
                ['.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','#','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.']]
    expected = (2,6)
    actual = find_start_point(input_rows)
    assert expected == actual

def test_day_6_find_start_point_invalid():
    input_rows = [['.','.','.','.','.','.','#','.','.','.','.','#','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.'],
                ['.','.','.','#','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','#','.','.','.'],
                ['.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','#','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.']]
    with pytest.raises(Exception) as e_info:
        find_start_point(input_rows)
        assert e_info.value == "No start point found"

def test_day_6_get_next_check_point_right():
    expected = (1,7)
    actual = get_next_check_point((1,6), '>')
    assert expected == actual

def test_day_6_get_next_check_point_left():
    expected = (1,5)
    actual = get_next_check_point((1,6), '<')
    assert expected == actual

def test_day_6_get_next_check_point_up():
    expected = (0,6)
    actual = get_next_check_point((1,6), '^')
    assert expected == actual

def test_day_6_get_next_check_point_down():
    expected = (2,6)
    actual = get_next_check_point((1,6), 'v')
    assert expected == actual

def test_day_6_get_next_check_point_invalid():
    with pytest.raises(Exception) as e_info:
        get_next_check_point((1,6), 'x')
        assert e_info.value == "Invalid direction"

def test_day_6_get_next_direction_right():
    expected = 'v'
    actual = get_next_direction('>')
    assert expected == actual

def test_day_6_get_next_direction_left():
    expected = '^'
    actual = get_next_direction('<')
    assert expected == actual

def test_day_6_get_next_direction_up():
    expected = '>'
    actual = get_next_direction('^')
    assert expected == actual

def test_day_6_get_next_direction_down():
    expected = '<'
    actual = get_next_direction('v')
    assert expected == actual

def test_day_6_get_next_direction_invalid():
    with pytest.raises(Exception) as e_info:
        get_next_direction((1,6), 'x')
        assert e_info.value == "Invalid direction"

def test_day_6_map_route():
    input_rows = [['.','.','.','.','.','.','#','.','.','.','.','#','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.'],
                ['.','.','.','#','.','.','^','.','.','.','.','.','.','.','#','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','#','.','.','.'],
                ['.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','#','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.']]
    expected = ([['.','.','.','.','.','.','#','.','.','.','.','#','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','X','X','X','X','X','X','#','.','.','.','.','.','.','.'],
                ['.','.','.','#','.','.','X','.','.','.','.','X','.','.','#','.','.','.','.','.'],
                ['.','.','.','X','X','X','X','#','.','.','.','X','.','.','.','.','#','.','.','.'],
                ['.','.','#','X','X','X','X','X','X','X','X','X','.','.','.','.','#','.','.','.'],
                ['.','.','.','.','.','.','X','.','.','.','.','#','.','.','.','.','#','.','.','.'],
                ['.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','#','.','.','.']], False)
    actual = map_route('^', (2,6), input_rows)
    assert expected == actual

def test_day_6_count_travelled_route():
    input_rows = [['.','.','.','.','.','.','#','.','.','.','.','#','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','X','X','X','X','X','X','#','.','.','.','.','.','.','.'],
                ['.','.','.','#','.','.','X','.','.','.','.','X','.','.','#','.','.','.','.','.'],
                ['.','.','.','X','X','X','X','#','.','.','.','X','.','.','.','.','#','.','.','.'],
                ['.','.','#','X','X','X','X','X','X','X','X','X','.','.','.','.','#','.','.','.'],
                ['.','.','.','.','.','.','X','.','.','.','.','#','.','.','.','.','#','.','.','.'],
                ['.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','#','.','.','.']]
    expected = 24
    actual = count_travelled_route(input_rows)
    assert expected == actual

def test_day_6_count_infinite_loops_for_row():  
    with Manager() as manager:
        loops_found = manager.Value('loops_found', 0)
        rows_checked = manager.Value('rows_checked', 0)
        input_rows = [['.','#','.','.','.','.','#'],
                    ['.','.','.','.','.','.','#'],
                    ['.','^','.','#','.','.','.'],
                    ['.','.','.','.','.','.','.'],
                    ['.','.','#','.','.','#','.']]
        expected = 1
        actual = count_infinite_loops_for_row(input_rows, 3, (2,1), '^', loops_found, manager.Lock(), rows_checked, manager.Lock())
        assert expected == actual

def test_day_6_count_infinite_loops_threaded_all_rows():  
    input_rows = [['.','#','.','.','.','.','#'],
                ['.','.','.','.','.','.','#'],
                ['.','^','.','#','.','.','.'],
                ['.','.','.','.','.','.','.'],
                ['.','.','#','.','.','#','.']]
    expected = 1
    actual = count_infinite_loops_threaded('^', (2,1), input_rows)
    assert expected == actual

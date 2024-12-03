import solution

def test_read_valid_input():
    expected_lists = ([1,5,8],[2,5,100])
    lists = solution.read_inputs('test_input.csv')
    assert expected_lists == lists

def test_read_valid_input_unsorted():
    expected_lists = ([8,5,1],[2,5,100])
    lists = solution.read_inputs('test_input.csv')
    assert expected_lists != lists

def test_get_valid_difference():
    expected_difference = 5
    actual_difference = solution.get_difference([1, 2, 3], [2, 2, 7])
    assert expected_difference == actual_difference

def test_get_valid_similarity():
    expected_similarity = 22
    actual_similarity = solution.get_similarity([1, 2, 3, 3, 4, 5, 6], [2, 2, 7, 4, 3, 4, 4])
    assert expected_similarity == actual_similarity

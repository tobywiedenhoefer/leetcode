from problems.problem_3 import length_of_longest_substring


def test_case_one():
    s = "abcabcbb"
    assert length_of_longest_substring(s) == 3


def test_case_two():
    s = "bbbbb"
    assert length_of_longest_substring(s) == 1


def test_case_three():
    s = "pwwkew"
    assert length_of_longest_substring(s) == 3


def test_case_four():
    s = "aab"
    assert length_of_longest_substring(s) == 2


def test_case_five():
    s = "dvdf"
    assert length_of_longest_substring(s) == 3

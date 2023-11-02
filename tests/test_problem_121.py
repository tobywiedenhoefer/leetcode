from problems.problem_121 import max_profit


def test_case_one():
    prices = [7, 1, 5, 3, 6, 4]
    output = max_profit(prices)
    assert output == 5


def test_case_two():
    prices = [7, 6, 4, 3, 1]
    output = max_profit(prices)
    assert output == 0

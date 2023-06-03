from main import CountingSort


def test_easy_sample():
    numbers = [5, 5, 1, 3]

    counting_algorithm = CountingSort(numbers)
    sorted_result = counting_algorithm.sort()

    assert sorted_result == ([1, 3, 5, 5] + [0] * (len(sorted_result)-len(numbers)))


def test_hard_sample():
    numbers = [0, 0, 1, 0, 0, 5, 5, 5, 6, 6, 6]

    counting_algorithm = CountingSort(numbers)
    sorted_result = counting_algorithm.sort()

    assert sorted_result == ([0, 0, 0, 0, 1, 5, 5, 5, 6, 6, 6])

""" Тесты к домашнему заданию 6"""

import pytest
from homework_6.lists_averages import ListsAverages
#from lists_averages import ListsAverages


@pytest.fixture
def first_list():
    """ Первый список"""
    return [1, 1, 1, 1, 1]


@pytest.fixture
def second_list():
    """ Второй список"""
    return [2, 2, 2, 2, 2]


@pytest.fixture
def empty_list():
    """ Третий список, пустой"""
    return []


@pytest.fixture
def not_numbers_list():
    """ Четвертый список, содержит не цифры"""
    return ["f", "s", "g"]


def test_first_bigger(second_list, first_list):
    """Первый список имеет большее среднее значение """
    la = ListsAverages(second_list, first_list)
    assert la.task() == "Первый список имеет большее среднее значение"


def test_second_bigger(first_list, second_list):
    """Второй список имеет большее среднее значение """
    la = ListsAverages(first_list, second_list)
    assert la.task() == "Второй список имеет большее среднее значение"


def test_averages_equal(second_list):
    """Средние значения списков равны """
    la = ListsAverages(second_list, second_list)
    assert la.task() == "Средние значения равны"


def test_empty_list(empty_list, first_list):
    """Один из списков пустой """
    la = ListsAverages(empty_list, first_list)
    assert la.task() == "Как минимум один из переданных списков пустой"


def test_first_list_with_not_numbers(first_list, not_numbers_list):
    """Первый список содержит не цифры """
    la = ListsAverages(not_numbers_list, first_list)
    assert la.task() == "В первом списке содержатся не только цифры"


def test_second_list_with_not_numbers(first_list, not_numbers_list):
    """Второй список содержит не цифры """
    la = ListsAverages(first_list, not_numbers_list)
    assert la.task() == "Во втором списке содержатся не только цифры"


def test_counting_averages_with_numbers_in_list(first_list):
    """ Верно ли функция ищет среднее значение в списке"""
    la = ListsAverages(first_list, first_list)
    assert la.count_average(la.list1) == 1


def test_counting_averages_with_empty_list(empty_list):
    """ Верно ли функция реагирует на пустой список"""
    la = ListsAverages(empty_list, empty_list)
    assert la.count_average(la.list1) == None


if __name__ == '__main__':
    pytest.main(['-v'])

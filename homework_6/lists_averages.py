# Задание 1. Создайте программу на Python или Java, которая принимает два списка чисел и выполняет следующие действия:
# a. Рассчитывает среднее значение каждого списка.
# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
# - ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
# - ""Средние значения равны"", если средние значения списков равны.
#
# Важно:
# Приложение должно быть написано в соответствии с принципами объектно-ориентированного программирования.
# Используйте Pytest (для Python) или JUnit (для Java) для написания тестов, которые проверяют правильность работы программы. Тесты должны учитывать различные сценарии использования вашего приложения.
# Используйте pylint (для Python) или Checkstyle (для Java) для проверки качества кода.
# Сгенерируйте отчет о покрытии кода тестами. Ваша цель - достичь минимум 90% покрытия.

import statistics
class ListsAverages:
    list1 : list[int]
    list2 : list[int]

    def __init__(self, list1:[int], list2:[int]):
        self.list1 = list1
        self.list2 = list2


    def count_average(self, list) -> float | None:
        if len(list) == 0:
            return None
        return statistics.mean(list)

    def task(self) -> str:
        result : String = " "
        if (len(self.list1) == 0 or len(self.list2) == 0):
            result = "Как минимум один из переданных списков пустой"
            return result
        ok : bool = True
        for element in self.list1:
            if not isinstance(element, int):
                ok = False
                result = "В первом списке содержатся не только цифры"
                return result
        for element in self.list2:
            if not isinstance(element, int):
                ok = False
                result = "Во втором списке содержатся не только цифры"
                return result
        if self.count_average(self.list1) > self.count_average(self.list2):
            result = "Первый список имеет большее среднее значение"
        elif self.count_average(self.list2) > self.count_average(self.list1):
            result = "Второй список имеет большее среднее значение"
        elif self.count_average(self.list2) == self.count_average(self.list1):
            result = "Средние значения равны"
        return result




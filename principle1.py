# 单一职责原则
from abc import abstractmethod


class Beverage:

    @abstractmethod
    def print_name(self):
        pass


class Coffee(Beverage):
    def print_name(self):
        print("coffee")


class Tea(Beverage):
    def print_name(self):
        print("tea")


c = Coffee()
c.print_name()
t = Tea()
t.print_name()

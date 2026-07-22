from utils.staff import Employee

# import pytest


def test_tut(some_calc, some_exp):
    emp1 = Employee("nonso", "asher", 10, "rais")
    emp2 = Employee("amanda", "asher", 8, "rais")

    assert emp1.age != some_calc * some_exp


def test_tusk(some_calc):
    emp1 = Employee("nonso", "asher", 10, "rais")
    emp2 = Employee("amanda", "asher", 8, "rais")

    assert emp2.age != some_calc

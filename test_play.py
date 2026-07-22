from utils.staff import Employee
import pytest


def test_tut():
    emp1 = Employee("nonso", "asher", 10, "rais")
    emp2 = Employee("amanda", "asher", 8, "rais")

    assert emp1.unit == emp2.unit

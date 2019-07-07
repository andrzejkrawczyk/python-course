__author__ = "Andrzej Krawczyk - Pep8 test"

import os
import sys
import json


class Punkt(object):

    def __init__(self, x, z, some_data):
        self.x = x
        self.z = z
        self.some_data = some_data

    def title(self):
        return "%s" % self.some_data


def some_data_processor(a, b, y=10, c=20, e=[1, 2, 3, 4]):
    result = 0
    for x in range(15):
        result = (a ** 2 + (c / y * e) + b ** b + 10 - 20 + 33 ** 2)
        if result % 2 == 0:
            print("oh!")


def foo(m, y, d="Ala ma kota", h="7 krasnali"):
    return d + h


def bar(a, b):
    return sum(a) / float(b)


some_results = foo(1, 2, d="zxc", h="askdj")

list_of_people = [
    "Rama",
    "John",
    "Shiva",
    "Janusz"
]

zdanieDoTestow = "To jest bardzo dluga linijka kodu zawierajaca po prostu jakis tekst o jakiejs dlugosci i chyba jest dosyc mocno za dluga"
Drugie_Zdanie = 'to jest kolejna dluga linijka tekstu do testow'

with open('/path/to/some/file/you/want/to/read') as file_1, \
        open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())

income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

wynik1 = "{} {} {}".format(zdanieDoTestow, 2, 3)

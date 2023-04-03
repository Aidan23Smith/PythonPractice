import unittest

from PersonBuilder import PersonBuilder
from PersonTest import check_person

GIVEN_NAME = "aidan"
FAMILY_NAME = "smith"
AGE = 25


class MyTestCase(unittest.TestCase):

    def test_default_values(self):
        check_person(self, PersonBuilder().build(), "", "", "")

    def test_build_person(self):
        person = PersonBuilder().set_given_name(GIVEN_NAME).set_family_name(FAMILY_NAME).set_age(AGE).build()
        check_person(self, person, GIVEN_NAME, FAMILY_NAME, AGE)


if __name__ == '__main__':
    unittest.main()

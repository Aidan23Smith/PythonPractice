import unittest

from Person import Person

GIVEN_NAME_1 = "Aidan"
GIVEN_NAME_2 = "Tom"
FAMILY_NAME = "Smith"
AGE = 25


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.person = Person("", "", "")

    def test_default_person(self):
        check_person(self, self.person, "", "", "")

    def test_change_given_name(self):
        self.person.change_given_name(GIVEN_NAME_1)
        check_person(self, self.person, GIVEN_NAME_1, "", "")

    def test_change_family_name(self):
        self.person.change_family_name(FAMILY_NAME)
        check_person(self, self.person, "", FAMILY_NAME, "")

    def test_change_age(self):
        self.person.change_age(AGE)
        check_person(self, self.person, "", "", AGE)

    def test_adding_two_people(self):
        person1 = Person("", "", "")
        person2 = Person("", "", "")

        person1.change_given_name(GIVEN_NAME_1)
        person2.change_given_name(GIVEN_NAME_2)

        check_person(self, person1, GIVEN_NAME_1, "", "")
        check_person(self, person2, GIVEN_NAME_2, "", "")


def check_person(self, person, given_name, family_name, age):
    self.assertEqual(person, Person(given_name, family_name, age))


if __name__ == '__main__':
    unittest.main()

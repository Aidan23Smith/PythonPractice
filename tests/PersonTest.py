import csv
import os
import unittest

from Person import Person

USER_ACCOUNT = 'user_account'
GIVEN_NAME_1 = "Aidan"
GIVEN_NAME_2 = "Tom"
FAMILY_NAME = "Smith"
AGE = 25
ID = "ID"


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.person = Person("", "", "")

    def tearDown(self):
        if os.path.isfile(USER_ACCOUNT):
            os.remove(USER_ACCOUNT)

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

    def test_person_is_saved(self):
        person1 = Person(GIVEN_NAME_1, FAMILY_NAME, AGE)
        person1.save(ID)
        with open(USER_ACCOUNT, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if (person1.given_name == row['given_name'] and
                        person1.family_name == row['family_name'] and
                        person1.age == int(row['age']) and
                        ID == row['_id']):
                    return
            self.assertTrue(False, "Person with attributes " + person1.given_name + " " + person1.family_name + " " + str(person1.age) + " " + ID + " was not found in the csv")


def check_person(self, person, given_name, family_name, age):
    self.assertEqual(person, Person(given_name, family_name, age))


if __name__ == '__main__':
    unittest.main()

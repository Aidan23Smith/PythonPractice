import csv
import os
import unittest
import uuid

from Person import Person
from Render import find_name, save_user_info, verify_user_account

USER_INFO = "user_info"
EMAIL1 = "a@a"
USERNAME1 = "a"
PASSWORD1 = "a"
EMAIL2 = "b@b"
USERNAME2 = "b"
PASSWORD2 = "b"

USER_NOT_FOUND = "user not found"
USER_ACCOUNT = 'user_account'
GIVEN_NAME_1 = "Aidan"
GIVEN_NAME_2 = "Tom"
GIVEN_NAME_3 = "john"
FAMILY_NAME = "Smith"
AGE = 25

ID1 = str(uuid.uuid4())
ID2 = str(uuid.uuid4())
ID3 = str(uuid.uuid4())


class MyTestCase(unittest.TestCase):

    def setUp(self):
        Person(GIVEN_NAME_1, FAMILY_NAME, AGE).save(ID1)
        Person(GIVEN_NAME_2, FAMILY_NAME, AGE).save(ID2)
        Person(GIVEN_NAME_3, FAMILY_NAME, AGE).save(ID3)
        self.ID1 = save_user_info(EMAIL1, USERNAME1, PASSWORD1)
        self.ID2 = save_user_info(EMAIL2, USERNAME2, PASSWORD2)

    def tearDown(self):
        if os.path.isfile(USER_ACCOUNT):
            os.remove(USER_ACCOUNT)

        if os.path.isfile(USER_INFO):
            os.remove(USER_INFO)

    def test_find_name_in_first_line(self):
        self.assertEqual(find_name(ID1), GIVEN_NAME_1)

    def test_find_name_in_last_line(self):
        self.assertEqual(find_name(ID3), GIVEN_NAME_3)

    def test_find_name_not_exist(self):
        self.assertEqual(find_name(str(uuid.uuid4())), USER_NOT_FOUND)

    def test_verify_user_account_in_last_line(self):
        self.assertEqual(verify_user_account(USERNAME1, PASSWORD1), self.ID1)

    def test_verify_user_account_wrong_password_or_username(self):
        self.assertFalse(verify_user_account(USERNAME1, PASSWORD2))

    def test_save_user_info_makes_file(self):
        if os.path.isfile(USER_INFO):
            os.remove(USER_INFO)
        save_user_info(EMAIL1, USERNAME1, PASSWORD1)
        self.assertTrue(os.path.isfile(USER_INFO))

    def test_save_user_info_saves_given_info(self):
        with open(USER_INFO, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if (EMAIL1 == row['email'] and
                        USERNAME1 == row['username'] and
                        PASSWORD1 == row['password']):
                    return
            self.assertTrue(False, "Person with information Email:" + EMAIL1 + " Username:" + USERNAME1 + " Password" + PASSWORD1 + " was not found in the csv")

    def test_save_user_info_returns_saved_id(self):
        user = save_user_info(EMAIL1, USERNAME1, PASSWORD1)
        with open(USER_INFO, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if user == row['_id']:
                    return
            self.assertTrue(False, "ID was not found")


if __name__ == '__main__':
    unittest.main()

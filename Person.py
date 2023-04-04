import uuid
import csv
import os.path

USER_ACCOUNT = 'user_account'


class Person:
    def __init__(self, given_name, family_name, age):
        self.given_name = given_name
        self.family_name = family_name
        self.age = age
        self.id = uuid.uuid4()

    def change_given_name(self, name):
        self.given_name = name

    def change_family_name(self, name):
        self.family_name = name

    def change_age(self, age):
        self.age = age

    def save(self):
        if not os.path.isfile(USER_ACCOUNT):
            with open(USER_ACCOUNT, 'a', newline="") as csvfile:
                fieldnames = ['given_name', 'family_name', 'age', 'id']
                writer = csv.DictWriter(csvfile, fieldnames)
                writer.writeheader()

        with open(USER_ACCOUNT, 'a', newline="") as csvfile:
            fieldnames = ['given_name', 'family_name', 'age', 'id']
            writer = csv.DictWriter(csvfile, fieldnames)

            writer.writerow({'given_name': self.given_name, 'family_name': self.family_name, 'age': self.age, 'id': self.id})

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.given_name == other.given_name and self.family_name == other.family_name and self.age == other.age
        return False


if __name__ == '__main__':
    person1 = Person("Aidan", "Smith", 25)
    print(person1.id)

    person2 = Person("Aidan", "Smith", 25)
    print(person2.id)

    person2.save()

class Person:
    def __init__(self, given_name, family_name, age):
        self.given_name = given_name
        self.family_name = family_name
        self.age = age

    def change_given_name(self, name):
        self.given_name = name

    def change_family_name(self, name):
        self.family_name = name

    def change_age(self, age):
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.given_name == other.given_name and self.family_name == other.family_name and self.age == other.age
        return False


if __name__ == '__main__':
    person1 = Person("Aidan", "Smith", 25)
    person2 = Person("Tom", "Powell", 18)

    person1.change_given_name("Aidan")
    person2.change_given_name("Tom")

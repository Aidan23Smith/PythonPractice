from Person import Person


class PersonBuilder:
    def __init__(self):
        self.given_name = ""
        self.family_name = ""
        self.age = ""

    def set_given_name(self, name):
        self.given_name = name
        return self

    def set_family_name(self, name):
        self.family_name = name
        return self

    def set_age(self, age):
        self.age = age
        return self

    def build(self):
        return Person(self.given_name, self.family_name, self.age)

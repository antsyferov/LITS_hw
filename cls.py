class Human:

    def __init__(self, name, last_name, sex, age):
        self.name = name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def __str__(self):
        return 'Human name {self.name} {self.last_name}, sex {self.sex},  age {self.age}'.format(self=self)

    def birthday(self):
        self.age += 1

class Man(Human):

    def __init__(self, name, last_name, age):
        super().__init__(name, last_name, 'M', age)

class Woman(Human):

    def __init__(self, name, last_name, age):
        super().__init__(name, last_name, 'F', age)

    def birthday(self):
         if self.age < 25:
            super().birthday()

john = Man('john', 'doe', 28)
marry = Woman('marry', 'doe', 28)
print(john)
print(marry)
john.birthday()
marry.birthday()

print(john)
print(marry)
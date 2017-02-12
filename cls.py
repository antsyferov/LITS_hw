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

class People(object):
    def __init__(self, lst=None):
        super(People, self).__init__()
        self.lst = lst or []
        
    def add_person(self, person):
        self.lst.append(person)

    def __iter__(self):
        return PeopleIterator(self)

class PeopleIterator:
    def __init__(self, col):
        self.col = col
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.col.lst):
            item = self.col.lst[self.idx]
            self.idx += 1
            return item
        raise StopIteration()

if __name__ == '__main__':
    lst = [Human('John', 'Doe', 'M', 25)]
    people = People(lst)
    jane = Human('Jane', 'Doe', 'F', 25)
    people.add_person(jane)
    for person in people:          
        print(person)

            

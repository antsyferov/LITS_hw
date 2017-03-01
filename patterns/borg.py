class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


b1 = Borg()
b2 = Borg()

b1.foo = 123

print(b2.foo)

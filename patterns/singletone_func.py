def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


class A(object):
    pass


@singleton
class LonelyClass(object):
    pass


a = LonelyClass()
b = LonelyClass()

print(a is b)

c = A()
d = A()

print(c is b)

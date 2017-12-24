class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.__sex__ = sex

    def __str__(self):
        return '姓名： %s\n年龄： %d' % (self.name, self.age)
    def info(self):
        print(self.name, self.age, self.__sex__)
class bjr(Person):
    def __str__(self):
        return str(bjr.__mro__)
a = bjr('xk', 24, 'mem')
print(a)
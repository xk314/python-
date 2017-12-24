
#python中以双下滑线开始和结束的方法为魔法方法，这是python自带的，
#可以通过重新定义来重写
class person(object):

    __country = '中国' #类属性
    __part = '共产党' #类的私有属性
    @classmethod   #通过修饰器定义类的方法
    def get(cls):
        return cls.__part

    def ch(self):
        self.__part = '国民党'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        # print(self.name)
        # print(self.age)
        print(self.__country)
        print(self.__part)

a = person('xk', 24)
b = person('xk1',25)
a.show()
b.show()
a.ch()
b.show()
a.show()


# zip map filter reduce
# zip 将一个或多的序列中的元素并排迭代出来,并返回一个迭代器
# map依次迭代序列中的每个元素并传入函数得到一个结果，每个元素对应一个结果，
#最后返回一个包含所有结果的可迭代对象。通过list可将其展开显示


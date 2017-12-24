

# 输出乘法表
def c_f_b():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print(' %d * %d = %-2d' % (j, i, i*j), end=' ')
            j += 1
        print('')
        # print('\n')  这样会打印两个换行
        i += 1

c_f_b()

# 通过迭代器获取有序序列的元素
#for循环配合迭代器使用时比while方便
for i in 'sfjoewjfewihgew':
    print(i.title(), end = ' ')

# import os
# print(os.system('dir'))

print()
def c_f_b1():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d * %d = %-2d  ' % (j, i, i*j), end = '')
        print('')
c_f_b1()

def my(a,*,b, c = 999):
    print(a)
    print(b)
    print(c)
my(1, b=2, c=3)
my_dict = {'name': 'xk', 'age': 24, 'sex': 'men'}
for i in my_dict:
    print(i)

a, *b = my_dict
print(a,b)



a = lambda x, y: x*y
a(1,2)
# 倒三角
for i in range(5,0,-1):
   # print(('* ' * i).center(30).strip())#贴边倒三角
    print(('* ' * i).center(30).rstrip())
#打印等腰倒三角，注意最小字符串单元为星号和一个空格。如果没空格，则会有偏移

num_list = [1, 2, 3, 4]
num = []
for i in num_list:
    for j in num_list:
        for k in num_list:
            if i != j and j != k and k != i:
                num.append(i * 100 + j *10 + k)
print('共有 %d 个数字' % len(set(num)))
print(num)

'''
start = 0
i = 5
while i > 0:
    end = 9 - (5 - i)
    start = start + (5 - i)
    list = [' ' for k in range(start - 1)]
    for j in range(start, end):
        item = '*' if (j + i) % 2 == 0 else ' '
        list.append(item)
    for item in list:
        print(item, end = ' ')
    i -= 1
    print('')
    '''

#a= [['s'] * 5]*5 可定义二维数组(列表)
#b = [[0] * 5] * 5  定义一个5*5 的列表，类似于二维数组


#星号第二种方法
#找到最合理的最小单位时，可简化难度
i = 1
space = 20
while i <= 5:
    for j in range(space + 5 - i):
        print(' ', end = '')
    for k in range(i):
        print('$ ', end = '')
    print('')
    i += 1
while i > 1:
    for j in range(space + 6 - i):
        print(' ', end= '')
    for k in range(i - 1):
        print('$ ', end = '')
    print('')
    i -= 1

# 按要求处理字符串
str1 = '1234567890'
# 1.截取字符串的第一位到第三位
print(str1[1:4])

# 截取字符串最后三位的字符
print(str1[-4:-1])   #执行切片操作是
# 截取字符串的全部字符
print(str1[:])
# 截取字符串的第七个字符到结尾
print(str1[7:])

# 截取字符串的第一位到倒数第三位之间的字符
print(str1[1:len(str1) - 3])
# 截取字符串的第三个字符
print(str1[3:4])

# 截取字符串的倒数第一个字符
print(str1[-1:-2:-1])

# 截取与原字符串顺序相反的字符串


# 截取字符串倒数第三位与倒数第一位之间的字符

# 截取字符串的第一位字符到最后一位字符之间的字符，每隔一个字符截取一次。



#求最大值最小值
num_list = [2,3,5,0,9,7,6543,76,432,87,423]
def max_min(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j],array[i]
    print('最大值为 %d   最小值为%d' % (array[-1], array[0]))
max_min(num_list)



#求最大值最小值
array = [2,3,5,0,9,7,6543,76,432,87,423]
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j],array[i]
print('最大值为 %d   最小值为%d' % (array[-1], array[0]))

#add方法可以将元素放入集合中，update可将序列拆开后放入集合
# 查看字符串中各个字符的个数
str = 'helloworldfheowghwoqghsadfhndsfuipwq'
str_set = set()
str_set.update(str)
str_num = {}
for i in str_set:
    str_num[i] = str.count(i)
for key, value in str_num.items():
    print(' %s  ： %d' % (key, value))


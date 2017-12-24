"""
def find_mixid(array):
    mix = array[0]
    mix_id = 0
    for i in array:
        if i < mix:
            mix = i
            mix_id = array.index(i)
    return mix_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        mix_id = find_mixid(array)
        new_array.append(array.pop(mix_id))
    return new_array
#选择排序的关键在于每次找到序列中最小或最大的那个元素的坐标，将其从原序列中弹出，
#并将其依次append到新的序列中，则这个新的序列就是已经排好序的序列。
a = [9,7,5,7,4,9,10,11,2,4,5,3,8]
print(search_sort(a))

a = [9,7,5,7,4,9,10,11,2,4,5,3,8]
#快排 递归
#快排算法每次将序列以一个值分割成大小两份，通过依次迭代使其最终有序
#迭代的关键在于选取好基线条件和迭代条件。通过基线条件结束迭代过程，通过迭代条件
#开始迭代过程
def quick_sort(array):
    if len(array) < 2: #当序列的元素个数不超过两个时，其一定是有序的
        return array   #一般情况下，此条件可作为迭代的基线条件
    mix = array[0]
    low = [i for i in array[1:] if i <= mix]
    big = [i for i in array[1:] if i > mix]
    return quick_sort(big) + [mix] + quick_sort(low)
    #此处开始进行迭代。没有显式的写出迭代条件
print(quick_sort(a))

a = [9,7,5,7,4,9,10,11,2,4,5,3,8]
'''
冒泡排序
双层循环嵌套。第一层循环的作用在于依次选取序列的每个元素，用其于序列中其他的
元素进行比较。第二层循环的作用在于让第一层选取的元素同其后面的所有元素依次比较。
通过两个元素的大小关系调整顺序。
第一层循环每执行一次，会从序列中找到一个最小的元素并使其排到最前面（使其冒泡出来）
'''
def m_P(array):
    for i in range(len(array)):
        for j in range(i + 1,len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
print(m_P(a))

i = 1
# for i in range(0, float('inf')):
# print( 'dddddd')


a = [9,7,5,7,4,9,10,11,2,4,5,3,8]
def get_mix(array):
    mix = array[0]
    mix_id = 0
    for i in array:
        if i < mix:
            mix = i
            mix_id = array.index(i)
    return mix_id

def search_sort1(array):
    new_array = []
    for i in range(len(array)):
        mix_id = get_mix(array)
        new_array.append(array.pop(mix_id))
    return new_array
print(search_sort(a))

a = [9,7,5,7,4,9,10,11,2,4,5,3,8]
def quick_sort1(array):
    if len(array) < 2:
        return array
    mix = array[0]
    low = [i for i in array[1:] if i <= mix]
    big = [i for i in array[1:] if i > mix]
    return quick_sort1(low) + [mix] + quick_sort1(big)
print(quick_sort1(a))

"""

'''
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def get_mix(array):
    mix_id = 0
    mix = array[0]
    for i in array:   #此处迭代序列的值为了找出本次序列中的最小值
        if i < mix:
            mix_id = array.index(i) #注意不要讲方法后面写成中括号
            mix = i
    return mix_id

def search_sort(array):
    new_array = []
    for i in range(len(array)):
        mix_id = get_mix(array)
        new_array.append(array.pop(mix_id)) #调用对象方法之前一定要创建对象
    return new_array

print(search_sort(a))
#列表可以在原处进行修改，

a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def quick_sort(array):
    if len(array) < 2:
        return array
    mix = array[0]
    low = [i for i in array[1:] if i <= mix]
    big = [i for i in array[1:] if i > mix]
    return quick_sort(low) + [mix] + quick_sort(big)
#快速排序  递归  基线条件  迭代条件
#列表的基线条件一般为len(list) < 2,此时不用对其在进一步的进行排序了
#列表的切片操作   下标从零开始  左闭右开    开始 结束 步长
#列表生成式
print(quick_sort(a))
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def m_p(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):#注意此处j的取值范围
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]#python中特有的值交换方法
    return array
#冒泡排序：序列的长度为len(array),外层循环共len(array),在每次外层循环中，
#使用目前序列中的第i个元素与后面的元素进行比较。找到目前序列中从i处往后的最小
# 的元素并将其移动到序列中的i处,即为冒泡。通过总共len(array)次的冒泡完成排序。
print(m_p(a))
'''


'''
def get_mix(array):
    mix_id = 0
    mix = array[0]
    for i in array:
        if i < mix:
            mix = i
            mix_id = array.index(i)
    return mix_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        mix_id = get_mix(array)
        new_array.append(array.pop(mix_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def quick_sort(array):
    if len(array) < 2:
        return array
    mix = array[0]
    low = [i for i in array[1:] if i <= mix]
    big = [i for i in array[1:] if i > mix]
    return quick_sort(low) + [mix] + quick_sort(big)
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))

'''
'''
def get_mix(array):
    mix_id = 0
    mix = array[0]
    for i in array:
        if i < mix:
            mix = i
            mix_id = array.index(i)
    return mix_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        mix_id = get_mix(array)
        new_array.append(array.pop(mix_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))
'''
'''
def get_mix(array):
    mix_id = 0
    mix = array[0]
    for i in array:
        if i < mix:
            mix = i
            mix_id = array.index(i)
    return mix_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        mix_id = get_mix(array)
        new_array.append(array.pop(mix_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i<= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))
'''
'''
def get_mix(array):
    mix_id = 0
    mix = array[0]
    for i in array:
        if i < mix:
            mix = i
            mix_id = array.index(i)
    return mix_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        mix_id = get_mix(array)
        new_array.append(array.pop(mix_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))
'''
'''
def get_mix(array):
    mix_id =0
    mix = array[0]
    for i in array:
        if i < mix:
            mix = i
            mix_id = array.index(i)
    return mix_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        mix_id = get_mix(array)
        new_array.append(array.pop(mix_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return  array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i> mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return  array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))
'''
'''
def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(i)
    return min_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))
#选择排序的时间为O(n*n)
def quick_sort(array):
    if len(array) < 2:
        return  array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))
#快速排序的时间为O(nlogn),最糟糕情况下快排的时间为O(n*n)
def m_p(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))


a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min, min_id = i, array.index(i)
    return min_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
print(search_sort(a))

a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def quick_sort(array):
    if len(array) < 2:
        return arrayd
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
print(quick_sort(a))

a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def m_p(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
print(m_p(a))


def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(i)
    return min_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
print(quick_sort(a))

a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def m_p(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
print(m_p(a))

a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(i)
    return min_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
print(search_sort(a))
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
print(quick_sort(a))
def m_p(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))

def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(i)
    return min_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
print(quick_sort(a))

a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def m_p(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
print(m_p(a))

a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(i)
    return min_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
print(search_sort(a))

a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
print(quick_sort(a))
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def m_p(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
    print(m_p(a))



def get_min(array):
     min_id = 0
     min = array[0]
     for i in array:
         if i < min:
             min = i
             min_id = array.index(i)
     return min_id

def search_sort(array):
     new_array = []
     for i in range(len(array)):
         min_id = get_min(array)
         new_array.append(array.pop(min_id))
     return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) +[mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))


def get_min(array):
    min = array[0]
    min_id = 0
    for i in array:
        if i < min:
            min = i
            min_id = array.index(i)
    return min_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i<= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))


def m_p(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))

def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(i)
    return min_id

def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))


def get_min(array):
    min = array[0]
    min_id = 0
    for i in array:
        if i < min:
            min = i
            min_id = array.index(i)
    return min_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))



def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(i)
    return min_id


def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))


def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))


def m_p(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))


def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(i)
    return min_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))


def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(min)
    return min_id

def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))

def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(min)
    return min_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))

def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i > min:
            min = i
            min_id = array.index(i)
    return min_id

def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))

def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(min)
    return min_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))


def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(min)
    return min_id

def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))

def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(min)
    return min_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))


def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(min)
    return min_id
def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))


def get_min(array):
    min_id = 0
    min = array[min_id]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(min)
    return min_id

def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

'''

def get_min(array):
    min_id = 0
    min = array[0]
    for i in array:
        if i < min:
            min = i
            min_id = array.index(min)
    return min_id

def search_sort(array):
    new_array = []
    for i in range(len(array)):
        min_id = get_min(array)
        new_array.append(array.pop(min_id))
    return new_array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(search_sort(a))

a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
def quick_sort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return quick_sort(low) + [mid] + quick_sort(big)
print(quick_sort(a))

def m_p(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
a = [9, 7, 5, 7, 4, 9, 10, 11, 2, 4, 5, 3, 8]
print(m_p(a))
my_list = [1, 3, 5, 7, 9, 11, 13]
'''
def binary_search(list, item):
    low = 0
    high = len(list) -1
    while low <= high:
        mid = (low + high) // 2
        #print(mid)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1   #
    return None
print(binary_search(my_list, 5))
#二分查找法的运行时间为O(log n),为对数时间

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid - 1
    return None
  
def binary_search(list,item):
    low, high = 0, len(list) - 1
    while low <=high:
        mid = (low + high) //2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return False
   
#二分查找法只适用于有序序列。通过逐渐缩小范围去判断元素是否存在于序列，并求出其索引。

def binary_search(list, item):
    low = 0
    high = len(list) -1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return False



def binary_search(my_list, item):
    low = 0
    high = len(my_list) -1
    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == item:
            print(mid)
            return True
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return False

def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return False
print(binary_search(my_list, 5))


def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return False

def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return False


def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low+high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return False

'''

def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low+high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return False
print(binary_search(my_list, 5))
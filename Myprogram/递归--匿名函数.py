def qucik_sort(array):
    if len(array) < 2:    #基线条件，结束递归
        return array      #递归条件，开始递归
    mid = array[0]        #基线和递归条件可以合并在一起
    low = [i for i in array[1:] if i <= mid]
    big = [i for i in array[1:] if i > mid]
    return qucik_sort(low) + [mid] + qucik_sort(big)
a = [7, 5, 7, 90, 4, 3, 42, 78, 54, 4, 3]
print(qucik_sort(a))



def j_c(num):
    if num >= 2:
        return num * j_c(num - 1)
    if num == 1:
        return 1
print(j_c(5))


f = lambda x, y : (x + y)
print(f(3, 4))
list1 = [[3, 8, 65, 65], [5, 3, 54, 54], [543, 65, 6, 654]]
print(list1.sort(key=lambda l: l[1]))
# print(list1)
a = [i for i in range(1,101)]
b = [a[i:i+3] for i in range(0,len(a) - 4,3)]
# print(b)




def m(a,b=[]):
    print(id(a))
    print(id(b))
# m(1,)
# m(2,)
# m(3,[1,])


a = {'name': 'xk', 'age': 24}
f = open('1.txt', 'r+', encoding='utf-8')
# f.write('fdsafweewfwe')
print(f.read())

# f.write(str(a) + '\n')
# f.write(str(a) + '\n')
# f.write(str(a) + '\n')
# print(f.readlines())
f.close()
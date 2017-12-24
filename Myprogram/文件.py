f = open('1.txt', 'r', encoding='utf-8')
# f = open('1.txt', 'r', encoding='utf-8')
ret = f.read(10)
# ret = f.readline(1024)
ret = f.readlines(1)
print(type(ret))
print(ret)

a = 'heima.txt'
b = a[:-4]
print(b)



num = 0
i = 1
while i <= 100:
    num = (num + i) if (i % 2) == 1 else (num - i)
    i += 1
# 加奇数减偶数


num = 0
i = 2
while i <= 100:
    if i % 2 == 1:
        num -= i
    else:
        num += i
    i += 1
print(num)


print(num)


tu=("alex",[11,22,{"k1":'v1',"k2":["age","name"],"k3":(11,22,33)},44])
print(id(tu))
tu[1][2]['k2'].append('fddddddddddddddddd')
print(tu[1][2]['k2'])
print(id(tu))

li=["alex","seven"]
b= dict([(i+10, j) for i, j in enumerate(li)])
print(b)


num = [11,22,33,44,55,66,77,88,99,90]
 # {'k1': 大于 66 的所有值,'k2': 小于 66 的所有值}

a = {}
a['k1'] = [i for i in num if i < 66]
a['k2'] = [i for i in num if i > 66]
print(a)
a = {}
a['k1'] = []
a['k2'] = []
for i in num:
    if i < 66:
        a['k1'].append(i)
    else:
        a['k2'].append(i)
print(a)


l1 = 'fjsfojweofojadosjfowe'
print(l1[9:-19:1])
l2 = [i for i in l1]

l1 = [[2,6,4,3], [54,76,352,6], [54,34,2,5]]
l1.reverse()
print(l1)
l1.sort()
print(l1)
l1.sort(key=lambda l : l[2])
print(l1)


t1 = (1,2,3,{1:3})
t1[3][2] = 3
print(t1)

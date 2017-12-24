
#您好！{'name': 'xk', 'age': 24}{'age': 24, 'name': 'xk'}
{'age': 24, 'name': 'xk'}

a = {'xk': {'姓名': 'xk', '电话': '18292488112', '地址': 'fdsf', '性别': '男', '年龄': '24'}}
print(type(a))

f = open('1.txt', 'r', encoding='utf-8')
# i = a['xk']
# info = '姓名 ' + i['姓名'] + ',' + '性别 ' + \
#     i['性别']  + ',' + '年龄 ' + i['年龄'] + ','\
#     + '电话 ' + i['电话'] + ',' \
#     + '地址 ' + i['地址']
# f.write(info)
a = f.read()

c = a.split(',')
print(c)
f.close()

print(list('姓名 xk'.split()))
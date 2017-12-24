my_dict = {'name': 'xk', 'age': '24', 'sex': '男'}

'''
字典的相关操作：
get     my_dict.get('key', '默认值')
获取字典中相关键对应的值，如果该键不在字典中，则返回默认值

setdefault   my_dict.setdefault('key', '默认值')
获取字典中指定的键所对应的值，如果该键不存在则返回默认值，并将该键和默认值添加到字典中
'''
print(my_dict.get('name'))
print(my_dict.setdefault('name1', 'xue'))
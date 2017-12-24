'''
列表中的元素是可以在原地修改的，比如增删改查
append：向列表中添加元素
extend：通过extend函数可以将另一个序列整体合并(元素依次)到列表中
insert：将元素插入到列表的指定位置（下标超过范围时插入到最后）
index，count：和字符串的相应函数功能相同（当查询的元素不存在时index会报错）
pop：默认弹出列表中的最后一个元素(指定元素的下标)
del：删除指定下标的元素（注意同名的列表方法和内置函数的区别）
remove：根据元素的值删除列表中的元素（只会删除列表中的相同元素的第一个）
sort：将列表按照指定的顺序重新排列，默认按照大小，参数reverse=True时可倒序排列
reverse：将列表逆置(列表也可支持[::-1]形式的逆置)


'''
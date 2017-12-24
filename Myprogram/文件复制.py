f = open('排序算法.py', 'r', encoding='utf-8')
f1 = open('排序算法复制.py', 'w', encoding='utf-8')
ret = '0'
# 文件复制，每次读取文件的一行，并将其写入另一个文件
while ret:
    ret = f.readline()
    f1.write(ret)
f.close()
f1.close()
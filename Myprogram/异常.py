import os
if os.path.exists('xk.txt'):
    os.remove('xk.txt')
try:
    f = open('xk.txt', 'r')
except FileNotFoundError as a:
    print('文件异常')
    print(a)
    f = open('xk.txt', 'w')



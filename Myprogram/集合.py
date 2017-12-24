for i in range(1,11):
    print(' ' * ((10 + i) // 2), end="")
    for j in range(1,1+i):
        if j > (10-i):
            continue
        print("$ ",end="")
    print()
'''
i = 5
space = 30
while i > 0:
    for j in range(space + i - 1):
        print(' ', end = '')
    for k in

    i -= 1
'''

a='''i -= 1
fds'''
b='''i -= 1
fds'''
print(len(a))
print(len(b))


def j_c(num):
    if num >= 2:
        return num * j_c(num - 1)
    if num == 1:
        return 1
print('aa')
print(j_c(0))
print('bb')
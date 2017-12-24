num1 = input('请输入一个数字：\n')
if not num1.isdigit():
    print('您必须输入一个数字！\n')
    exit(1)
num2 = input('请再输入一个数字：\n')
if not num2.isdigit():
    print('您必须输入一个数字！\n')
    exit(1)
print('您输入的两个数字之和为 %d\n' % (int(num1) + int(num2)))
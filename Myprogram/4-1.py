num = input('请输入两个数字：\n').split()
if not num[0].isdigit() or not num[1].isdigit():
    print('您必须输入两个数字！\n')
    exit(1)
print('您输入的两个数字之和为 %d\n' % (int(num[0]) + int(num[1])))
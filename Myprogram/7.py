name = input('请输入您的姓名：')
qq = input('请输入您的qq号：')
while not qq.isdigit():
    qq= input('请正确输入您的qq号!')
number = input('请输入您的手机号:')
while not number.isdigit():
    number = input('请正确输入您的手机号!')
dizhi = input('请输入您的公司地址：')
print('=' * 35)
print('姓名:%s' % name)
print('QQ:%s' % qq)
print('手机号:%s' % number)
print('公司地址:%s' % dizhi)
print('=' * 35)
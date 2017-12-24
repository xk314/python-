import os
show_item = '''
1.添加名片    2.删除名片
3.修改名片    4.查询名片
5.退出系统
'''
func_dict = {1: 'self.add1()', 2: 'self.del_info()', 3: 'self.change_info()',\
                4: 'self.search()', 5: 'down_sys()'}
class Card_Gover(object):
    def __init__(self):
        self.card_dic = {}
        self.show = show_item
        self.file = '名片1.txt'
        self.fun_dict = func_dict
    def uplaod(self):
        if not os.path.exists(self.file):
            f = open(self.file, 'w', encoding='utf-8')
            f.close()
        f = open(self.file, 'r', encoding='utf-8')
        ret = f.read()
        if len(ret) == 0:
            ret = '{}'
        self.card_dic = eval(ret)
        f.close()
    def save(self):
        f = open(self.file, 'w+', encoding='utf-8')
        f.write(str(self.card_dic))
        f.close()
    def show_select(self):
        num = input(self.show)
        if num.isdigit() and 0 < int(num) < 6:
            return int(num)
        else:
            print('您输入的数据有误！')
            self.show_select()

    def add1(self):
        str = input('请输入如下信息： 姓名  年龄 电话(以空格间隔)')
        if len(str.split()) != 3:
            print('请按正确格式输入')
            return
        name, age, phone = str.split()
        if name in self.card_dic.keys():
            print('已有该用户名，请重新输入！')
            return
        if name.isalpha() and age.isdigit() and phone.isdigit():
            self.card_dic[name] = {}
            self.card_dic[name]['姓名'] = name
            self.card_dic[name]['年龄'] = int(age)
            self.card_dic[name]['电话'] = int(phone)
        else:
            print('请按正确格式输入！')

    def del_info(self):
        if len(self.card_dic) == 0:
            print('当前系统用户为零！')
            return None
        str = input('请输入姓名：')
        if str.isalpha():
            if str in self.card_dic.keys():
                del self.card_dic[str]
                print('成功删除%s！' % str)
            else:
                print('您输入的名字不在系统中！')
                return

    def change_add(self, str):
        str = input('请联系人的最新信息： 姓名  年龄 电话(以空格间隔)')
        if len(str.split()) != 3:
            print('请按正确格式输入！')
            return
        name, age, phone = str.split()
        if name is not str:
            print('两次输入的姓名不一致！')
            return None
        if name.isalpha() and age.isdigit() and phone.isdigit():
            self.card_dic[name] = {}
            self.card_dic[name]['姓名'] = name
            self.card_dic[name]['年龄'] = int(age)
            self.card_dic[name]['电话'] = int(phone)
            return True
        else:
            print('请按正确格式输入！')

    def change_info(self):
        if len(self.card_dic) == 0:
            print('当前系统用户为零！')
            return
        str = input('请输入要修改的联系人的姓名：')
        if str.isalpha():
            if str in self.card_dic.keys():
                if self.change_add(str):
                    print('成功修改%s！' % str)
                else:
                    print('修改联系人失败！')
                    return False
            else:
                print('您输入的名字不在系统中！')
                return

    def print_info(self,info_dict):
        print('姓名： %s' % info_dict['姓名'])
        print('年龄： %d' % info_dict['年龄'])
        print('电话： %d' % info_dict['电话'])
    def search(self):
        str = input('请输入姓名：')
        if len(self.card_dic) == 0:
            print('当前系统用户为零！')
            return
        if str.isalpha():
            if str in self.card_dic.keys():
                info_dict = self.card_dic[str]
                self.print_info(info_dict)
            else:
                print('您输入的名字不在系统中！')
                return
    def down_sys(self):
        self.save()
        exit(0)

    def main(self):
        self.uplaod()
        while True:
            num = self.show_select()
            eval(self.fun_dict[num])
            self.save()




a = Card_Gover()
a.main()
'''
添加名片
删除名片
修改名片
查询名片
退出系统
'''

graph = '''
1.添加名片    2.删除名片
3.修改名片    4.查询名片
5.退出系统
'''
add_show = '''
请按照格式输入信息：姓名 电话 地址 性别 年龄（以空格隔开）
'''
fun_dic = {'1': 'add()', '2': 'del1()', '3': 'change()', '4': 'search()',\
           '5': 'download_info()'}
card_dic = {}
# ['姓名 xk', '性别 男', '年龄 24', '电话 18292488112', '地址 fdsf']
def upload_date():
    '''
    将存储于文本文件的名片信息加载到内存
    :return: 
    '''
    global card_dic
    f = open('名片.txt', 'r',encoding='utf-8')
    for line in f.readlines():
        line = line.split(',')
        # print(line)
        # print(line[0])
        name = line[0].split()[1]  #得到名片中的人名
        card_dic[name] = {}  #为每个人创建字典
        for item in line[:len(line)]:
            key = item.split()[0]
            value = item.split()[1]
            card_dic[name][key] = value
    f.close()


def download_info():
    '''
    将当前存在于内存中的名片信息写入磁盘
    :return: 
    '''
    global card_dic
    f = open('名片.txt', 'w', encoding='utf-8')
    for key, item in card_dic.items():
        print(key, item)
        print(type(item))
        info = '姓名 ' + item['姓名'] + ',' + '性别 ' + \
                item['性别'] + ',' + '年龄 ' + item['年龄'] + ','\
                + '电话 ' + item['电话'] + ',' \
                + '地址 ' + item['地址']
        print(info)
        print(type(info))
        f.write(info)
        f.write('\n')
    f.close()
    exit(0)



def jug_info(str):
    str_list = str.split(' ')
    if len(str_list) != 5:
        print('请按照正确格式输入信息！')
        return False
    if not str_list[0].isalpha():
        print('姓名格式错误！')
        return False
    if (not str_list[1].isdigit()) and len(str_list[1]) != 11:
        print('电话的格式错误！')
        return False
    if not str_list[2].isalnum():
        print('地址格式错误！')
        return False
    if str_list[3] not in ['男', '女']:
        print('性别格式错误！')
        return False
    if not str_list[4].isdigit() or\
                    int(str_list[4]) not in range(2,100):
        print('年龄格式错误!')
        return False
    return True

def jude_dic():
    global card_dic
    if len(card_dic) == 0:
        print('当前系统共0个用户！')
        return False
    return True

def  insert_info_dic(list):
    global card_dic
    info = {}
    print('开始添加数据')
    info['姓名'] = list[0]
    info['电话'] = list[1]
    info['地址'] = list[2]
    info['性别'] = list[3]
    info['年龄'] = list[4]
    card_dic[list[0]] = info
    print('添加数据成功')
    return True

def insert_dic(str):
    global card_dic
    str_list = str.split(' ')
    if str_list[0] in card_dic.keys():
        print('当前系统已有该用户！')
        return False
    insert_info_dic(str_list)
    print('添加成功11111')
    return True


def add():
    global add_show
    input_str = input(add_show)
    if not jug_info(input_str):
        return False
    if not insert_dic(input_str):
        return False
    print('添加信息成功！')
    print(card_dic)
    return True


def del1():
    global card_dic

    if not jude_dic():
        return False
    str_input = input('请输入您要删除的联系人姓名：')
    if not str_input.isalpha():
        print('姓名格式错误！')
        return False
    if str_input not in card_dic.keys():
        print('您输入的姓名不在系统内！')
        return False
    del card_dic[str_input]
    print('成功删除 %s' % str_input)
    return True


def change():
    global card_dic
    if not jude_dic():
        return False
    str_input = input('请输入您要修改的联系人姓名：')
    if not str_input.isalpha():
        print('姓名格式错误！')
        return False
    if str_input not in card_dic.keys():
        print('您输入的姓名不在系统内！')
        return False
    need_change = str_input
    print('该用户在系统中，请继续：')
    str_input = input('请按照格式输入信息：\
    姓名 电话 地址 性别 年龄（以空格隔开）')
    if not jug_info(str_input):
        return False
    del card_dic[need_change]
    str_list = str_input.split(' ')
    insert_info_dic(str_list)
    print('修改 %s 用户信息完成！' % str_list[0])
    print(card_dic[str_list[0]])
    return True


def print_info(str):
    global card_dic
    for key, value in card_dic[str].items():
        print(' %s  :  %s' % (key, value))


def search():
    global card_dic
    if not jude_dic():
        return False
    str_input = input('请输入你要查询的姓名：')
    if not str_input.isalpha():
        print('请正确输入姓名！')
        return False
    if str_input not in card_dic.keys():
        print('您输入的用户不在系统中！')
        return False
    print(' %s 的信息如下：' % str_input)
    print_info(str_input)



def show():
    global graph
    while True:
        num_str = input('请输入功能序号：' + graph)#多次输入回车会出错
        if not num_str.isdigit():
            continue
        if int(num_str) not in range(1, 6):
            print('请输入您选择的功能的序号！')
        else:
            return int(num_str)


def main():
    global fun_dic
    upload_date()
    while True:
        num = show()
        eval(fun_dic[str(num)])


main()
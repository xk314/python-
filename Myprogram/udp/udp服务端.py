import socket
'''
# ip = '192.168.155.127'
ip = '192.168.115.51'  #  在window环境下的ip
port = 8088
address = (ip, port)
socket_file = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_file.bind(address)
date, add = socket_file.recvfrom(1024)
print('从 %s 收到数据 %s' % (add, date.decode()))   #从win环境下接受的数据必须通过gbk解码才能显示
socket_file.sendto('服务端向你发送的数据'.encode(), add)
socket_file.close()

#win环境下的软件默认以gbk编码格式对数据中的中文进行解码和编码，和win下的网络调试工具通信时以gbk格式编码
#win下pycharm中编写的程序默认以utf-8编码解码数据中的中文
win下调试助手发送的汉字以gbk形式编码，在linux或pycharm下要显示时需以gbk形式解码。
linux环境下的网络调试助手发送的汉字以utf-8形式编码
'''
'''
host_ip = '192.168.115.51'
port = 8888
address = (host_ip, port)
socket_file = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_file.bind(address)
# date, add = socket_file.recvfrom(124)
date = socket_file.recvfrom(124)
print(date)
print(type(date))
# print('从 %s 收到数据： %s' % (add, date.decode()))
# socket_file.sendto('服务器端向客户端发送数据'.encode(), add)
socket_file.close()
'''
'''
ser_ip = '192.168.115.61'
port = 8094
ser_addr = (ser_ip, port)
recv_len = 102
socket_file = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_file.bind(ser_addr)
while True:
    date, addr = socket_file.recvfrom(recv_len)
    print(' %s  :  %s ' % (addr, date.decode()))
    date = input('请输入向客户端发送的数据：')
    if date == 'q':
        break
    socket_file.sendto(date.encode(), addr)
socket_file.close()
'''
'''
ser_ip = '192.168.115.61'
port = 9999
ser_addr = (ser_ip, port)
socket_file = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_file.bind(ser_addr)

class Server()
'''
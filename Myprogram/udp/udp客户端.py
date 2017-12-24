import socket
'''
socket_file = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ('192.168.115.51', 8088)    #注意此处的端口号需使用int类型，若使用字符串格式将报错
date = input('请输入数据：')
socket_file.sendto(date.encode(), server)
rec_date, add1 = socket_file.recvfrom(1024)
print('从 %s  收到数据： %s' % (add1, rec_date.decode()))
socket_file.close()
'''
'''
ser_ip = '192.168.115.51'
port = 8888
ser_addr = (ser_ip, port)
socket_file = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
date = input('请输入向服务端发送的数据：')
socket_file.sendto(date.encode(), ser_addr)
date, addr = socket_file.recvfrom(124)
print('从 %s 接受到数据： %s' % (addr, date.decode()))
socket_file.close()
'''

# udp客户端程序
ser_ip = '192.168.115.61'   #在局域网中这个ip地址每天会变
port = 8080
ser_addr = (ser_ip, port)
recv_len = 1
socket_file = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    date = input('请输入项服务端发送的数据：')
    if date == 'q':
        break
    socket_file.sendto(date.encode(), ser_addr)
    date, addr = socket_file.recvfrom(recv_len)
    print('  %s :  %s ' % (addr, date.decode()))
socket_file.close()












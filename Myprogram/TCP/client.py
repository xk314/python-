'''
import socket
ser_ip = '192.168.115.61'
port = 8887
ser_addr = (ser_ip, port)
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(ser_addr)
print('ssssssssssssssss')
while True:
    date = input('请输入要发送的数据：')
    tcp_socket.send(date.encode())
    print('已发送')
    date = tcp_socket.recv(1024)
    print(ser_ip + ' : ' + date.decode())
'''

import socket
ser_ip = ('192.168.115.52', 8889)
ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser_socket.bind(ser_ip)
ser_socket.listen(128)
client_socket, client_addr = ser_socket.accept()
print('xxxxx')
while True:
    date = client_socket.recv(1024)
    if date :
        print('收到来自 %s 的信息： %s' % (client_addr, date.decode()))
    else:
        # print(' %s 断开了连接' % client_addr)
        print(client_addr, end='')
        print('   断开了连接')
        client_socket.close()
        break
    date = input('请输入要发送的数据：')
    client_socket.send(date.encode())
ser_socket.close()
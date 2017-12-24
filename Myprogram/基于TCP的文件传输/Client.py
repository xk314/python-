import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = input('请输入服务端的ip地址：')
port = eval(input('请输入端口号：'))
client_socket.connect((ip, port))
while True:
    date = input('请输入要发送的数据：')
    client_socket.send(date.encode())
    date = client_socket.recv(1024)
    if date:
        print('收到来自 %s 的信息： %s' % (ip, date.decode()))
    else:
        print('%s 断开了连接'% ip)
        break
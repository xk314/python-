import socket
ser_ip = '192.168.115.61'
port = 8889
ser_addr = (ser_ip, port)
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#创建服务端的监听套接字
tcp_socket.bind(ser_addr)
#服务端绑定端口
tcp_socket.listen(122)   #监听
#服务端对客户端的连接请求进行监听
print('listen')
client_socket, client_addr = tcp_socket.accept()
#在此阻塞等待客户端的连接。连接成功后，返回和客户端建立了连接的套接字及客户端的地址
while True:
    date = client_socket.recv(1024)
    print(str(client_addr) + '  :  ' + date.decode())
    date = input('请输入要发送的数据：')
    client_socket.send(date.encode())

client_socket.close()
tcp_socket.close()


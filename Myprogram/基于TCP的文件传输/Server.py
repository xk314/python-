import socket, os
class Server(object):
    __ser_ip = ''
    __listen_num = 128
    # __port = 8888
    # __ser_addr = (__ser_ip, __port)

    def __init__(self, port=8888):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(Server.__ser_ip, port)
        self.server_socket.listen(Server.__listen_num)
        self.client_socket = ''
        self.client_address = ''

    def server_accept(self):
        self.client_socket, self.client_address = self.server_socket.accept()

    def server_recv(self):
        while True:

            self.client_socket.send(('选择你要下载的文件：' + '\n' + os.system('ls -l ')).encode())
            date = self.client_socket.recv()
            if not date:
                print('用户 %s 下线' % self.client_address)
                self.client_socket.close()
                break
            else:
                file_name = date.decode()
                if os.path.isfile(file_name):
                    self.send_file(file_name)
                else:
                    self.client_socket.send('你输入的文件不存在！'.encode())

    def send_file(self, file_name):
        file = open(file_name, 'rb')
        self.client_socket.send(file.read())
        file.close()
    def __del__(self):
        self.client_socket.close()
        self.server_socket.close()



class Client(object):
    ser_ip = ''
    def __init__(self, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




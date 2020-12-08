# 1、定义socket（套件字）对象
# 2、和服务端建立连接
# 3、发送数据
# 4、接收数据
# 5、关闭客户端套件字

import socket

if __name__ == '__main__':
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(('192.168.1.37', 8080))
    send_data = '你好服务器，我是老黑'.encode('gbk')
    tcp_client_socket.send(send_data)
    rec_data = tcp_client_socket.recv(1024)
    print(rec_data)
    data = rec_data.decode('gbk')
    print(data)
    tcp_client_socket.close()

# 1、创建套件字对象
# 2、连接服务端
# 3、发送数据
# 4、接收数据
# 5、关闭套件字

import socket

if __name__ == '__main__':
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(('192.168.1.37', 8080))
    tcp_client_socket.send('你好，小妞'.encode('gbk'))
    # 此处111为一次接收的字节数
    data = tcp_client_socket.recv(111)
    recv_data = data.decode('gbk')
    print(recv_data)
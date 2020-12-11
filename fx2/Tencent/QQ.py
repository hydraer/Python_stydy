import socket
if __name__ == '__main__':
    # 1、定义套件字
    QQ_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、和服务端建立连接
    QQ_socket.connect(('192.168.1.37', 8080))
    # 3、发送数据
    send_data = '你好，老白'.encode('gbk')
    QQ_socket.send(send_data)
    # 4、接收数据
    data = QQ_socket.recv(1024)
    recv_data = data.decode('gbk')
    print(recv_data)
    # 5、关闭套件字
    QQ_socket.close()
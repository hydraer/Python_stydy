import socket
import threading

def recv_message(server_sockt, ip_port):
    

if __name__ == '__main__':

    # 1、定义套件字对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、设置端口复用、绑定端口
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('', 9090))
    # 3、设置监听
    server_socket.listen(128)
    # 4、等待客户端连接
    service_client_socket, ip_port = server_socket.accept()
    print('客户端的ip为：', ip_port)
    # 5、接收数据
    data = service_client_socket.recv(1024)
    recv_data = data.decode('gbk')
    print('接收的数据为：', recv_data)
    # 6、发送数据
    send_data = '欢迎来到腾讯世界'.encode('gbk')
    service_client_socket.send(send_data)
    # 7、关闭套件字
    service_client_socket.close()
    server_socket.close()

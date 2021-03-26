# 1、创建套件字对象
# 2、绑定端口号（绑定前设置端口复用）
# 3、设置监听
# 4、等待客户端连接
# 5、接收数据
# 6、发送数据
# 7、关闭套件字

import socket
import threading

def handle_client_question(server_socket, tcp_port):
    print('收到客户问题反馈，客户为：', ip_port)
    data = server_socket.recv(1024)
    recv_data = data.decode('gbk')
    if recv_data:
        print(recv_data)
        send_data = '黄河黄河，我是长江'.encode('gbk')
        server_socket.send(send_data)
    else:
        print('客户端已关闭')
    server_socket.close()

if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 9090))
    tcp_server_socket.listen(128)
    while True:
        server_socket, ip_port = tcp_server_socket.accept()
        handle_thread = threading.Thread(target=handle_client_question, args=(server_socket, tcp_server_socket))
        handle_thread.setDaemon(True)
        handle_thread.start()
    tcp_server_socket.close()
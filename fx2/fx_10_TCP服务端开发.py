# 1、设置套件字对象
# 2、绑定端口号(先设置端口复用）
# 3、设置监听
# 4、等待客户端连接请求
# 5、接收数据
# 6、发送数据
# 7、关闭套件字

import socket

if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 8080))
    tcp_server_socket.listen(128)

    service_client_socket, ip_port = tcp_server_socket.accept()

    print('客户端IP地址和端口号', ip_port)
    recv_data = tcp_server_socket.recv(1024)

    reve_content = recv_data.decode('gbk')
    print('接收到的数据为：', reve_content)

    send_data = '已收到，问题正在处理中'.encode('gbk')

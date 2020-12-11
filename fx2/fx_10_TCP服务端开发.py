# 1、设置套件字对象
# 2、绑定端口号(先设置端口复用）
# 3、设置监听
# 4、等待客户端连接请求
# 5、接收数据
# 6、发送数据
# 7、关闭套件字

import socket

if __name__ == '__main__':
    # 1、定义套件字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 3、绑定端口号
    tcp_server_socket.bind(('', 8989))
    # 4、设置监听
    tcp_server_socket.listen(128)
    # 5、等待客户端连接请求
    service_client_socket, ip_port = tcp_server_socket.accept()
    # 6、接收数据
    print('客户端IP地址和端口号', ip_port)
    recv_data = service_client_socket.recv(1024)

    reve_content = recv_data.decode('gbk')
    print('接收到的数据为：', reve_content)
    # 7、发送数据
    send_data = '已收到，问题正在处理中'.encode('gbk')
    service_client_socket.send(send_data)
    # 8、关闭套件字
    service_client_socket.close()
    tcp_server_socket.close()

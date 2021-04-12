# 1、 HTTP 协议的全称是(HyperText Transfer Protocol)，翻译过来就是超文本传输协议。
# 2、 HTTP 协议的作用：规定了浏览器和 Web 服务器通信数据的格式，也就是说浏览器和web服务器通信需要使用http协议

import socket
import os

if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 9000))
    tcp_server_socket.listen(128)
    while True:
        client_socket, ip_port = tcp_server_socket.accept()
        recv_client_data = client_socket.recv(1024)
        recv_client_condent = recv_client_data.decode('utf-8')
        print(recv_client_condent)
        with open("static\grand.html", "rb") as file:
            file_data = file.read()
        reponse_line = 'HTTP/1.1 200 OK\r\n'
        reponse_header = 'Server:PWS1.0\r\n'
        reponse_body = file_data
        reponse_data = (reponse_line + reponse_header + '\r\n').encode('utf-8') + reponse_body
        client_socket.send(reponse_data)
        client_socket.close()
    tcpserver_socket.close()

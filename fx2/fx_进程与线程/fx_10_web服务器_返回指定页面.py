import socket

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 9999))
    tcp_server_socket.listen(128)
    while True:
        new_socket, ip_port = tcp_server_socket.accept()
        client_data = new_socket.recv(1024)
        if len(client_data) == 0:
            print('用户关闭了浏览器')
            new_socket.close()
            return
        recv_client_content = client_data.decode('utf-8')
        print(recv_client_content)
        request_list = recv_client_content.split(' ', maxsplit = 2)
        request_path = request_list[1]
        print(request_path)
        if request_path == "/":
            request_path = '/index.html'
        try:
            with open('static' + request_path, 'rb') as file:
                file_data = file.read()
        except Exception as e:
            request_line = 'HTTP/1.1 404 Not Found\r\n'
            request_header = 'Server:PWS1.0\r\n'
            with open('static/error.html') as file:
                request_body = file.read()
            request_data = (request_line + request_header + "/r/n").encode('utf-8') + request_body
            new_socket.send(request_data)
            new_socket.close()
        else:
            request_line = 'HTTP/1.1 200 OK\r\n'
            request_header = 'Server:PWS1.0\r\n'
            request_body = file_data
            request_data = (request_line + request_header + '\r\n').encode('utf-8') + request_body
            new_socket.send(request_data)
            new_socket.close()

if __name__ == '__main__':
    main()
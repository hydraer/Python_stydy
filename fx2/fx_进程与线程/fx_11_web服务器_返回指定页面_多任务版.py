import socket
import threading

def handle_client_request(new_socket, ip_port):
    recv_data = new_socket.recv(4096)

    if len(recv_data) == 0:
        print('客户端已断开')
        return
    recv_content = recv_data.decode('utf-8')
    recv_list = recv_content.split(' ', maxsplit=2)
    request_path = recv_list[1]
    if request_path == '/':
        request_path = '/index.html'
    try:
        with open('static' + request_path, 'rb') as file:
            file_data = file.read()
    except Exception as e:
        request_line = 'HTTP/1.1 404 NOT FOUND\r\n'
        request_header = 'Server:PWS1.0\r\n'
        with open('static/error.html', 'rb') as file:
            file_data = file.read()
        request_body = file_data
        request_content = (request_line + request_header +'\r\n').encode('utf-8') + request_body
        new_socket.send(request_content)
    else:
        request_line = 'HTTP/1.1 200 OK\r\n'
        request_header = 'Server:PWS1.0\r\n'
        request_body = file_data
        request_content = (request_line + request_header + '\r\n').encode('utf-8') + request_body
        new_socket.send(request_content)
        new_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 9999))
    tcp_server_socket.listen(128)
    while True:
        new_socket, ip_port = tcp_server_socket.accept()
        print(f'客户端{ip_port}已连接')
        client_thread = threading.Thread(target=handle_client_request, args=(new_socket, ip_port))
        client_thread.start()

if __name__ == '__main__':
    main()

import socket
import threading

class HttpWebServer(object):
    def __init__(self):
        tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_socket_server.bind(('', 9898))
        tcp_socket_server.listen(128)
        self.tcp_socket_server = tcp_socket_server
    @staticmethod
    def handle_client_data(new_socket, ip_port):
        print(f'与客户端：{ip_port}连接')
        recv_data = new_socket.recv(1024)
        if len(recv_data) == 0:
            print('客户端断开连接')
            new_socket.close()
            return
        recv_content = recv_data.decode('utf-8')
        recv_list = recv_content.split(' ', maxsplit=2)
        recv_path = recv_list[1]
        if recv_list[1] == '/':
            recv_path = '/index.html'
        try:
            with open('static' + recv_path, 'rb') as file:
                recv_data = file.read()
        except Exception as e:
            reponse_line = 'HTTP/1.0 404 NOT FIND\r\n'
            reponse_header = 'Server:PWS1.0\r\n'
            with open('static/error.html', 'rb') as file:
                recv_data = file.read()
            reponse_body = recv_data
            reponse_content = (reponse_line + reponse_header + '\r\n') + reponse_body
            new_socket.send(reponse_content)

        else:
            reponse_line = 'HTTP/1.0 200 OK\r\n'
            reponse_header = 'Server:PWS1.0\r\n'
            reponse_body = recv_data
            reponse_content = (reponse_line + reponse_header + '\r\n').encode('utf-8') + reponse_body
            new_socket.send(reponse_content)
        finally:
            new_socket.close
    def start(self):
        while True:
            new_socket, ip_port = self.tcp_socket_server.accept()
            threading1 = threading.Thread(target=self.handle_client_data, args=(new_socket, ip_port))
            threading1.setDaemon(True)
            threading1.start()

def main():
    http_server = HttpWebServer()
    http_server.start()

if __name__ == '__main__':
    main()
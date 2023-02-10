# CLIENT
import socket
import ssl
import sys


class sslClient:

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.sendMessage()

    def sendMessage(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_verify_locations('cert.pem')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:

            with context.wrap_socket(sock, server_hostname=self.hostname, server_side=False) as ssock:
                ssock.connect((ssock.server_hostname, self.port))
                print("\nConnected to the server")
                msg = input("\nEnter a message to send to the server: ")
                ssock.sendall(str.encode(msg))
                print("\nClient Terminated\n")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Please enter input as: python3 SslCli.py <server_domain> <port_number>")
        sys.exit()
    host = sys.argv[1]
    port = int(sys.argv[2])
    serv = sslClient(host, port)
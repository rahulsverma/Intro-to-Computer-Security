# SERVER
import socket
import ssl
import sys


class sslServer:

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.getRequest()

    def getRequest(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain('cert.pem', 'key.pem')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
            sock.bind((self.hostname, self.port))
            sock.listen(1)
            print("\nServer listening at: " + self.hostname + ":" + str(self.port))

            with context.wrap_socket(sock, server_side=True) as ssock:
                conn, addr = ssock.accept()
                print("\nClient connected " + str(addr))
                client_message = conn.recv(1024).decode('utf-8')
                print("\nMessage from client: " + client_message)
                print("\nServer Terminated\n")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please enter input as: python3 SslServ.py <port_number>")
        sys.exit()
    host = socket.gethostname()
    port = int(sys.argv[1])
    serv = sslServer(host, port)
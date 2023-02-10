Name: Rahul Verma

Email: rverma4@binghamton.edu

Programming language used: Python

Code was tested on remote.cs

Steps to execute the program:(pem pass phrase is not required)
1) Place the cert and key files in the same folder as the "SslServ.py" and "SslCli.py" files.
2) Create 2 sessions for Server and for Client.
3) For Server(SslServ.py) input as "python3 SslServ.py <port_number>".
4) For Client(SslCli.py) input as "python3 SslCli.py <server_domain> <port_number>".

Certificate was generated using this command:
openssl req -x509 -nodes -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
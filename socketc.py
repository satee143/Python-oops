from socket import  *
host=gethostname()
port=8087
s=socket()
s.connect((host,port))
s.send(b'hello server')
msg=s.recv(1024)

print(msg)
s.close()
from socket import  *
host=gethostname()
port=8087
s=socket()
s.bind((host,port))
print('server started')
s.listen(5)
c,a=s.accept()
print('connection established')
msg=c.recv(1024)
print(msg)
c.send(b'hello client')
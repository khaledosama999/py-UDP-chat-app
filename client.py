import socket 

MAX_SIZE_BYTES = 65535

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('127.0.0.1',3000))
print('Client socket address', format(s.getsockname))

while True :
    message = input("")
    data = message.encode('ascii')

    s.send(data)

    data, address = s.recvfrom(MAX_SIZE_BYTES) 
    dataDecoded = data.decode('ascii')

    print('message {}',format(dataDecoded))
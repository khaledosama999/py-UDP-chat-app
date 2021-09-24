import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to and address and port
port = 3000
hostname = "127.0.0.1"
MAX_BYTE_SIZE = 65535

s.bind((hostname,port))


print('Listing at {}',format(s.getsockname()))

while True :
    data, clientAddress = s.recvfrom(MAX_BYTE_SIZE)
    
    clientMessageDecoded = data.decode('ascii')
    print("message: {}", format(clientMessageDecoded))

    reply = input("")
    replyEncoded = reply.encode("ascii");

    s.sendto(reply,clientAddress)


import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientIPs = [] # Store client IPs so we know where to send messages.
sock.bind(('',11221))

while True:
    print("Server started")
    msgBytes, clientIP = sock.recvfrom(2048)
    actualMessage = msgBytes.decode()
    if not str.find(actualMessage.lower(),"has joined the server.") == -1:
       clientIPs.append(clientIP) # Adds you to the list if you join.
       for otherClientIP in clientIPs:
          sock.sendto(msgBytes,(otherClientIP, 11256)) 

        
    elif not str.find(msg_recebida,"has left the server.") == -1:
       client_ips.remove(clientIP) # Tells you to get out if you leave.
        for otherClientIP in clientIPs:
          sock.sendto(msgBytes,(otherClientIP, 11256)) 

    else:
        for otherClientIP in clientIPs:
          sock.sendto(msgBytes,(otherClientIP, 11256)) 

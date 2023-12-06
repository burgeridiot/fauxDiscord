import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_ips = [] # Store client IPs so we know where to send messages.
sock.bind(('',11221))

while True:
    print("Server started")
    msg_bytes, id_ip = sock.recvfrom(2048)
    msg_recebida = msg_bytes.decode().lower()
    print(msg_recebida)
    if not str.find(msg_recebida,"has joined the server.") == -1:
       client_ips.append(id_ip) # Adds you to the list if you join.
       for ipt in client_ips:
          sock.sendto(msg_bytes,(ipt, 11256)) 

        
    elif not str.find(msg_recebida,"has left the server.") == -1:
       client_ips.remove(id_ip) # Tells you to get out if you leave.
       for ipt in client_ips:
          sock.sendto(msg_bytes,(ipt, 11256)) 

    else:
       for ipt in client_ips:
          sock.sendto(msg_bytes,(ipt, 11256)) 

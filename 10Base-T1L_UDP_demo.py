import socket
import time

UDP_IP = "192.168.1.28"
UDP_PORT = 5005
MESSAGE = b"Hello, World!1739874019273409172341628736418723641623946128346182634871628346182364816238463287"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
                     
                     
while 1:
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	time.sleep(1)
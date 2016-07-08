#! /usr/bin/python
import socket
import sys
import fcntl
import struct
from getId import getId
def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915,
		struct.pack('256s',ifname[:15])
	)[20:24])

UDP_IP = ''
UDP_PORT =7070 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
sock.bind((UDP_IP, UDP_PORT))
while True:
	data, addr = sock.recvfrom(1024)
	print data		
	if data == "pi":
		try:
			myip = get_ip_address("eth0")
		except:
			myip = "no LAN connection"
		finally:
			MESSAGE = getId() + " " +  myip
		print str(addr)
		print MESSAGE
		sock.sendto(MESSAGE, addr)

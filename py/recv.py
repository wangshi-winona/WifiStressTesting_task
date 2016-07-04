#! /usr/bin/python
import fcntl
import struct
import socket
def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915,
		struct.pack('256s',ifname[:15])
	)[20:24])

UDP_IP = get_ip_address("wlan0")
UDP_PORT = 7070

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
sock.bind((UDP_IP, UDP_PORT))
while True:
	data, addr = sock.recvfrom(1024)
	print data

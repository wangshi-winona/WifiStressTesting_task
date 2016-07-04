#! /usr/bin/python
import fcntl
import struct
import socket
from getId import getId
def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915,
		struct.pack('256s',ifname[:15])
	)[20:24])

UDP_IP = '175.159.2.175'
UDP_PORT = 10100

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
MESSAGE = getId() + " " + get_ip_address("wlan0")
sock.sendto(MESSAGE,(UDP_IP, UDP_PORT))

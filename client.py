#!/usr/bin/python

import sys
import socket
import argparse

parser = argparse.ArgumentParser(description='Pass some file.')
parser.add_argument("filename", type=str)
parser.parse_args()

s = socket.socket()
host = "192.168.1.2"
port = 12345
s.connect((host,port))

try:
    f = open(sys.argv[1], 'rb')
    print "Sending..."
    l = f.read(1024)
    while (l):
        s.send(l)
        l = f.read(1024)
    f.close()
    print "Done Sending"
    s.shutdown(socket.SHUT_WR)
    print s.recv(1024)
    s.close()

except IOError:
    print "Please enter vald filename."

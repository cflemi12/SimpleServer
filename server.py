#!/usr/bin/python

#@author Chase Fleming
#@date 10/3/15
#simple server that accepts data from any client
#and stores it in a subdirectory. 

import socket
import os
import uuid

#make new directory "recieved" if it doesn't already exist. 
DIR_NAME = "recieved"
if not os.path.exists(DIR_NAME):
    os.makedirs(DIR_NAME)
    print "New subdirectory made."

s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(1)

try:
    while True:
        c, addr = s.accept()
        print "Got connection from", addr
        print "Recieving..."
        filename = str(uuid.uuid4())
        f = open(os.getcwd()+'/'+DIR_NAME+'/'+filename, 'wr')
        l = c.recv(1024)
        while (l):
            f.write(l)
            l = c.recv(1024)
        print "Done Recieving"
        f.close()
        c.close()

except KeyboardInterrupt:
    print "\nKeyboard intterrupt recieved. Stopping Server."
    s.close()

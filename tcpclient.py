#!/usr/bin/env python
# -*- coding:utf8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import socket

class NetClient(object):
    def tcpclient(self, command):
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSock.connect(('192.168.31.16', 80))
        #clientSock.connect(('192.168.31.25', 32009))

        sendDataLen = clientSock.send(command)
        recvData = clientSock.recv(1024)
        print "sendDataLen: ", sendDataLen
        print "recvData: ", recvData
        
        clientSock.close()

if __name__ == "__main__":
    netClient = NetClient()
    command = sys.argv[1]
    print (command)
    netClient.tcpclient(command)
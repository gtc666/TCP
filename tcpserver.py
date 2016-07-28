#!/usr/bin/env python
# -*- coding:utf8 -*-

import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

import socket

class NetServer(object):
    def tcpServer(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('192.168.31.25', 32010))       # 绑定同一个域名下的所有机器
        sock.listen(5)
        with open("deviceIP.txt","w") as f:
            f.write("name : ip address\n")
            f.close()
        
        while True:
            clientSock, (remoteHost, remotePort) = sock.accept()
            print("[%s:%s] connect" % (remoteHost, remotePort))     # 接收客户端的ip, port
            
            revcData = clientSock.recv(1024)
            print "revcData: ", revcData
            print "remoteHost: ", remoteHost
            with open("deviceIP.txt","r") as f:
                lines = f.readlines()
                try:
                    position = lines.index(revcData + ": " + remoteHost + "\n")
                except ValueError:
                    f.close()
                    with open("deviceIP.txt","a") as f:
                        f.write(revcData + ": " + remoteHost + "\n")
                        f.close()
                        print ("This IP Address is a new one, register")
                else:
                    f.close()
                    print ("This IP Address has already registered")
            sendDataLen = clientSock.send("got. --from server")
            clientSock.close()


if __name__ == "__main__":
    netServer = NetServer()
    netServer.tcpServer()

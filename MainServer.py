#coding:utf-8
import ServerConfig #导入服务器配置文件
global s #初始化部分全局变量
s = 0
global data
data = 0
from socket import *
from time import  ctime
import  threading
import time
host = ServerConfig.Server_IP
port = ServerConfig.Server_Port
ADDR = (host,port)
serverlooptick = True
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(ServerConfig.Server_max_listen)
socks=[]                             #放每个客户端的socket

def handle(): #SOCKET部分
    while True:
        global s
        for s in socks:
            try:
                data = s.recv(ServerConfig.Server_BUFSIZ)     #到这里程序继续向下执行
            except Exception, e:
                continue
            if not data:
                socks.remove(s)
                continue
            s.send('[%s],%s' % (ctime(), data))

def Mainserver(): #服务端部分
    print "Server Loaded!"
    while serverlooptick:
     if not ServerConfig.Server_Password and data:
        s.send('Server-Version:1.0-test')
        if data == 'ClientOK':
          s.send('Data-Started')
        else:
            if data and data == ServerConfig.Server_Password_ID:
                s.send('Server-Version:1.0-test')
                if data == 'ClientOK':
                 s.send('Data-Started')



t = threading.Thread(target=handle)
t1 = threading.Thread(target=Mainserver)       #子线程
if __name__ == '__main__':   
    t.start()
    t1.start()
    print 'waiting for connecting...' #SOCKET部分
    while True:
        clientSock,addr = tcpSerSock.accept()
        print  'connected from:', addr
        clientSock.setblocking(0)
        socks.append(clientSock)

 #form CSDN User Mr.Jing
 #版权声明：本文为CSDN博主「惊瑟」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
 #原文链接：https://blog.csdn.net/qq_34062683/article/details/78063035

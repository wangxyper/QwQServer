#coding:utf-8
import ServerConfig #导入服务器配置文件
global s #初始化部分全局变量
s = 0
global data
data = 0
from socket import * #导入依赖
from time import  ctime
import  threading
import time
host = ServerConfig.Server_IP #定义服务端IP&&端口
port = ServerConfig.Server_Port
ADDR = (host,port)
serverlooptick = True #无用变量
tcpSerSock=socket(AF_INET,SOCK_STREAM) #固定服务端地址&&监听部分
tcpSerSock.bind(ADDR)
tcpSerSock.listen(ServerConfig.Server_max_listen) 
socks=[]                             #放每个客户端的socket
RunCommand = os.system #调用系统指令的变量

def handle(): #SOCKET（服务端SOCKET通信）部分
    while True:
        global s #定义变量S为全局变量
        for s in socks: #for循环
            try:
                data = s.recv(ServerConfig.Server_BUFSIZ)     #到这里程序继续向下执行 #定义data为服务端接收到的数据
            except Exception, e: 
                continue #向下继续
            if not data: #超时断开
                socks.remove(s)
                continue #向下继续
            s.send('[%s],%s' % (ctime(), data)) #发送时间戳

def Mainserver(): #服务端部分
    print "Server Loaded!" #打印Server Loaded
    while ServerConfig.Server_Loop_Tick: #服务端循环TICK
     if not ServerConfig.Server_Password and data:
        s.send('Server-Version:1.0-test')
        if data == 'ClientOK':
          s.send('Data-Started')
          if data == 'Run0Server':
                     RunCommand('screen -dmS SERVER .java/bin/java -Xmx12G -server -jar server.jar') #调用系统指令
        else:
            if data and data == ServerConfig.Server_Password_ID:
                s.send('Server-Version:1.0-test')
                if data == 'ClientOK':
                 s.send('Data-Started')
                 if data == 'Run0Server':
                     RunCommand('.java/bin/java -Xmx12G -server -jar server.jar') #调用系统指令


#为服务端和SOCKET部分创建线程
t = threading.Thread(target=handle)
t1 = threading.Thread(target=Mainserver)       #子线程
if __name__ == '__main__':  #初始化  
    t.start()
    t1.start()
    print 'waiting for connecting...' #SOCKET部分
    while True: #非阻塞式accept
        clientSock,addr = tcpSerSock.accept()
        print  'connected from:', addr
        clientSock.setblocking(0)
        socks.append(clientSock)

 #form CSDN User Mr.Jing
 #版权声明：本文为CSDN博主「惊瑟」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
 #原文链接：https://blog.csdn.net/qq_34062683/article/details/78063035

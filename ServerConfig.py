#coding:utf-8
Server_Port = 2154 #服务端端口
Server_IP = '' #服务端监听地址
Server_max_listen = 2048 #最多连接数
Server_BUFSIZ = 1024 #每次最大接收的字节数
Server_Loop_Tick = True #是否启用服务端的默认tick循环 #警告：如果设为false，则服务端部分只会检测一次，不会循环检测，禁用此项会出现问题
Server_Password = False #是否启用服务器密码
Server_Password_ID = '123456' #服务器密码

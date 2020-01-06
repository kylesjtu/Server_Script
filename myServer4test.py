# coding:utf-8

from socket import *
from time import ctime
import time
import struct

print("=====================时间戳TCP服务器=====================");
def ConfigServer():
    HOST = '127.0.0.1'  # 主机号为空白表示可以使用任何可用的地址。
    PORT = 4444  # 端口号
    BUFSIZ = 1024  # 接收数据缓冲大小
    ADDR = (HOST, PORT)

    tcpSerSock = socket(AF_INET, SOCK_STREAM)  # 创建TCP服务器套接字
    tcpSerSock.bind(ADDR)  # 套接字与地址绑定
    tcpSerSock.listen(5)  # 监听连接，同时连接请求的最大数目
    print('参数服务器等待客户端的连接...')
    while True:
        tcpCliSock, addr = tcpSerSock.accept()  # 接收客户端连接请求
        print('参数服务器取得连接:', addr)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        a=struct.pack('>h',233)
        print(a)
        tcpCliSock.send(struct.pack('>h',233))
        while True:
            data = tcpCliSock.recv(BUFSIZ)  # 连续接收指定字节的数据，接收到的是字节数组
            print("byte类数据", data)
            if data==b'\xfa\x5e':
                tcpCliSock.send(data)
                print('key接收成功，并返回key')
            # data=struct.unpack('>h', data)
            # print("short类数据",data)

            if data==b'\xaa':
                tcpCliSock.send(struct.pack('>h',1))
                print("已返回连接反馈信号")
            #print("字符串数据",result)
            if not data:  # 如果数据空白，则表示客户端退出，所以退出接收
                break
            # tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))
            #tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))  # 向客户端发送时间戳数据，必须发送字节数组

        tcpCliSock.close()  # 关闭与客户端的连接
        print("参数连接已关闭")
    tcpSerSock.close()  # 关闭服务器socket

def DataServer():
    HOST = '127.0.0.1'  # 主机号为空白表示可以使用任何可用的地址。
    PORT = 4445  # 端口号
    BUFSIZ = 1024  # 接收数据缓冲大小
    ADDR = (HOST, PORT)

    tcpSerSock = socket(AF_INET, SOCK_STREAM)  # 创建TCP服务器套接字
    tcpSerSock.bind(ADDR)  # 套接字与地址绑定
    tcpSerSock.listen(5)  # 监听连接，同时连接请求的最大数目
    print('数据服务器等待客户端的连接...')
    while True:
        tcpCliSock, addr = tcpSerSock.accept()  # 接收客户端连接请求
        print('数据服务器取得连接:', addr)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        tcpCliSock.send(struct.pack('>h', 233))
        while True:
            data = tcpCliSock.recv(BUFSIZ)  # 连续接收指定字节的数据，接收到的是字节数组
            print("byte类数据", data)
            if data == b'\xfa\x5e':
                tcpCliSock.send(data)
                print('key接收成功，并返回key')
            # data=struct.unpack('>h', data)
            # print("short类数据",data)

            if data == b'\xaa':
                tcpCliSock.send(struct.pack('>h', 1))
                print("已返回连接反馈信号")
            # print("字符串数据",result)
            if not data:  # 如果数据空白，则表示客户端退出，所以退出接收
                break
            # tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))
            # tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))  # 向客户端发送时间戳数据，必须发送字节数组

        tcpCliSock.close()  # 关闭与客户端的连接
        print("数据连接已关闭")
    tcpSerSock.close()  # 关闭服务器socket
    print("数据服务器已关闭")
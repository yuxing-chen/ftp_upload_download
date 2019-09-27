# Author:xichen
# @Time:2019/9/1120:09
import socket
import os,sys
import json
import struct
sys.path.append(os.path.dirname(__file__))
from core import src
from.interface import common_interface

xichen = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
xichen.bind(('192.168.11.78',8006))
xichen.listen(5)
func_msg = {'1':'注册','2':'登录','3':'上传文件','4':'下载文件'}
func_msg_dic = bytes(json.dumps(func_msg),'utf8')
func_msg_len = len(func_msg_dic)
func_msg_head = struct.pack('i',func_msg_len)
while True:
    conn,addr = xichen.accept()
    while True:
        # 向客户端发送头部长度
        conn.send(func_msg_head)
        # 向客户端发送头部内容
        conn.send(func_msg_dic)

        user_choice = conn.recv(1).decode('utf8')
        if user_choice == 'q':
            break
        if user_choice == '1':
            src.register()
        elif user_choice == '2':
            src.login()
        elif user_choice == '3':
            common_interface.download()
        elif user_choice == '4':
            common_interface.upload()
















# Author:xichen
# @Time:2019/9/1120:12
import os,sys,json
import socket,struct
sys.path.append(os.path.dirname(__file__))
from core import src
from interface import common_interface

user = socket.socket()
user.connect(('192.168.11.78',8006))
while True:
    # 接收服务端发送的4个字节的头部长度
    head_len = struct.unpack('i', user.recv(4))[0]

    # 就收服务端发送的头部内容
    func_msg = json.loads(user.recv(head_len))
    for k,v in func_msg.items():
        print(f'{k}:{v}')
    user_choice = input('请选择功能:')
    user.send(user_choice.encode('utf8'))
    if user_choice == '3':
        common_interface.download()
    elif user_choice == '4':
        common_interface.upload()











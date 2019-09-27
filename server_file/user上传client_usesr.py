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
    if user_choice == 'q':
        break
    if user_choice == '1':
        src.register()
    elif user_choice == '2':
        src.login()
    elif user_choice == '3':
        file_name,file_head,file_dic = common_interface.upload()
        # 发送四个字节
        user.send(file_head)
        # 发送头部内容
        user.send(file_dic)
        with open(file_name,'rb') as f:
            for line in f:
                user.send(line)
        print('文件上传成功')

    elif user_choice == '4':
        file_choice = common_interface.file_interface()
        user.send(str(file_choice).encode('utf8'))
        # 接收文件头的四个字节，并转换格式
        file_head = struct.unpack('i',user.recv(4))[0]
        # 接收文件头部内容
        file_dic = json.loads(user.recv(file_head))
        l = file_dic['size']
        file_name = file_dic['name']
        count = 0
        data = b''
        if not os.path.isdir('client_file'):
            os.mkdir('client_file')
        file_path = os.path.join('client_file', file_name)
        with open(file_path,'wb') as f:
            while count < l:
                if l < 1024:
                    data_temp = user.recv(l)
                else:
                    if l-count >= 1024:
                        data_temp = user.recv(1024)
                    else:
                        data_temp = user.recv(l-count)
                data += data_temp
                count += len(data_temp)
            f.write(data)
        print('文件下载成功')












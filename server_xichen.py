# Author:xichen
# @Time:2019/9/1120:09
import socket
import os,sys
import json
import struct
sys.path.append(os.path.dirname(__file__))
from core import src
from interface import common_interface

xichen = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
xichen.bind(('192.168.11.78',8006))
xichen.listen(5)
func_msg = {'1':'注册','2':'登录','3':'上传文件','4':'下载文件'}
func_msg_dic = bytes(json.dumps(func_msg),'utf8')
func_msg_len = len(func_msg_dic)
func_msg_head = struct.pack('i',func_msg_len)
while True:
    print('等待客户端连接')
    conn,addr = xichen.accept()
    print(f'客户端已连接{addr}')
    while True:
        try:
            # 向客户端发送头部长度
            conn.send(func_msg_head)
            # 向客户端发送头部内容
            conn.send(func_msg_dic)

            user_choice = conn.recv(1).decode('utf8')

            # 客户端上传文件
            if user_choice == '3':
                # 接收客户端的四个字节
                head = conn.recv(4)
                # 取出头部的长度
                head_len = struct.unpack('i',head)[0]
                # 接收客户端发送的头部内容
                head_dic = json.loads(conn.recv(head_len))
                # print(head_dic)
                l = head_dic['size']
                file_name = head_dic['name']
                count = 0
                data = b''
                if not os.path.isdir('server_file'):
                   os.mkdir('server_file')
                file_path = os.path.join('server_file',file_name)
                with open(file_path, 'wb') as f:
                    while count < l:
                        if l < 1024:
                            data_temp = conn.recv(l)
                        else:
                            if l - count >= 1024:
                                data_temp = conn.recv(1024)
                            else:
                                data_temp = conn.recv(l - count)
                        data += data_temp
                        count += len(data_temp)
                    f.write(data)
                print(f'{addr}成功上传文件')

            # 客户端下载文件
            elif user_choice == '4':
                file_choice = conn.recv(1).decode('utf8')
                file_name,file_head,file_dic = common_interface.download(int(file_choice))
                # 发送文件头四个字节
                conn.send(file_head)
                # 发送文件头部内容
                conn.send(file_dic)
                with open(file_name,'rb') as f:
                    for line in f:
                        conn.send(line)

                print(f'{addr}下载文件成功')
        except Exception:
            break
    conn.close()

xichen.chose()





















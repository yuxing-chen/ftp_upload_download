# Author:xichen
# @Time:2019/9/1412:56
import os,sys,json,struct
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from conf import settings
file_list = os.listdir(settings.FILE_PATH)

def file_interface():
    while True:
        for file_number,file_name in enumerate(file_list):
            print(f'{file_number}:{file_name}')
        file_choice = input('选择下载文件:')
        if file_choice == 'q':
            break
        file_choice = int(file_choice)
        return file_choice




def download(file_choice):
        # 计算发送给客户端的头的长度
        file_dic = {'size':os.path.getsize(file_list[file_choice]),'name':f'user下载{file_list[file_choice]}'}
        # 转换二进制格式
        file_b = bytes(json.dumps(file_dic),'utf8')
        # 获取头的长度,并且转换为4个字节
        file_head_len = struct.pack('i',len(file_b))

        return file_list[file_choice],file_head_len,file_b


def upload():
    while True:
        for file_number,file_name in enumerate(file_list):
            print(f'{file_number}:{file_name}')

        # 选择上传的文件
        file_choice = input('选择上传文件:')
        if file_choice == 'q':
            break
        file_choice = int(file_choice)

        # 计算发送给客户端的头的长度
        file_dic = {'size':os.path.getsize(file_list[file_choice]),'name':f'user上传{file_list[file_choice]}'}
        # 转换二进制格式
        file_b = bytes(json.dumps(file_dic),'utf8')
        # 获取头的长度,并且转换为4个字节
        file_head_len = struct.pack('i',len(file_b))

        return file_list[file_choice],file_head_len,file_b








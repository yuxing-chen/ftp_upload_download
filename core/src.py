# Author:xichen
# @Time:2019/9/1120:10
from interface import user_interface

user_info = {'name':None}

# 用户注册功能
def register():
    while True:
        user_name = input('输入注册用户名:')
        if user_name == 'q':
            break
        pwd = input('输入用户密码:')
        re_pwd = input('确认用户密码:')
        if re_pwd == pwd:
            flag,msg = user_interface.register_interface(user_name, pwd)
            print(msg)
            if flag:
                break
            else:
                continue
        else:
            print('两次密码不一致！')
            continue


# 用户登录功能
def login():
    while True:
        user_name = input('输入注册用户名:')
        if user_name == 'q':
            break
        pwd = input('输入用户密码:')
        flag,msg = user_interface.login_interface(user_name,pwd)
        print(msg)
        if flag:
            user_info['name'] = user_name
            break
        else:
            continue





# Author:xichen
# @Time:2019/9/1120:56

from db import modlers

# 用户注册接口
def register_interface(name,pwd):
    user_self =modlers.User.select(name)
    if not user_self:
        modlers.User(name,pwd)
        return True,'用户注册成功！'
    else:
        return False,'用户已经存在了！'


# 用户登录接口
def login_interface(name,pwd):
    user_self = modlers.User.select(name)
    if not user_self:
        return False,'用户不存在！'
    else:
        if user_self.pwd == pwd:
            return True,'用户登录成功'
        else:
            return False,'用户密码错误！'


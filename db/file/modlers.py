# Author:xichen
# @Time:2019/9/1120:39

from db import db_handlers

# 客户注册用户的基类
class Base:
    def save(self):
        db_handlers.save(self)

    @classmethod
    def select(cls,name):
        self = db_handlers.select(cls,name)
        return self


# 用户类
class User(Base):
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd
        self.save()

# # 客户端文件类
# class Client_file(Base):
#     def __init__(self,name):
#
# # 服务端文件类


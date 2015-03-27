# -*- coding: cp936 -*-

import pickle
import hashlib

open("key.dat", "a")
s = open("key.dat").read()

try:
    accounts = pickle.loads(s)
except:
    accounts = {}

for username, md5p in accounts.items():
    if md5p:
        print username


while True:
    tips = """
============================
创建新用户请输入   1
修改用户密码请输入 2
删除用户请输入     3
退出请输入         4
"""
    print tips
    c = raw_input().strip()

    if c == "1":
        username = raw_input("请输入用户名：").strip()
        if accounts.get(username):
            print "该用户已存在"
        else:
            password = raw_input("请输入密码：").strip()
            md5p = hashlib.md5(password).hexdigest()
            accounts[username] = md5p
    elif c == "2":
        username = raw_input("请输入要修改密码的用户名：").strip()
        if not accounts.get(username):
            print "该用户不存在"
        else:
            password = raw_input("请输入密码：").strip()
            md5p = hashlib.md5(password).hexdigest()
            accounts[username] = md5p
    elif c == "3":
        username = raw_input("请输入要删除的用户名：").strip()
        if not accounts.get(username):
            print "该用户不存在"
        else:
            accounts[username] = ""
    elif c == "4":
        break
    
    open("key.dat", "w").write(pickle.dumps(accounts))



    

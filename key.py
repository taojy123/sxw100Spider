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
�������û�������   1
�޸��û����������� 2
ɾ���û�������     3
�˳�������         4
"""
    print tips
    c = raw_input().strip()

    if c == "1":
        username = raw_input("�������û�����").strip()
        if accounts.get(username):
            print "���û��Ѵ���"
        else:
            password = raw_input("���������룺").strip()
            md5p = hashlib.md5(password).hexdigest()
            accounts[username] = md5p
    elif c == "2":
        username = raw_input("������Ҫ�޸�������û�����").strip()
        if not accounts.get(username):
            print "���û�������"
        else:
            password = raw_input("���������룺").strip()
            md5p = hashlib.md5(password).hexdigest()
            accounts[username] = md5p
    elif c == "3":
        username = raw_input("������Ҫɾ�����û�����").strip()
        if not accounts.get(username):
            print "���û�������"
        else:
            accounts[username] = ""
    elif c == "4":
        break
    
    open("key.dat", "w").write(pickle.dumps(accounts))



    

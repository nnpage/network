#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 16:02
# @Author  : Aries
# @Site    : 
# @File    : test04.py
# @Software: PyCharm
from test03 import SSH

ssh = SSH()

with open("ip_list.txt") as f:
    for ips in f.readlines():
        # print(ips)
        ssh.login_to_device(ip=ips.strip())
        ssh.get_hostname()
        ssh.backup_config()

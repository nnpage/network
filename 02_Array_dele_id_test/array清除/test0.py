#!/usr/bin/env python3
# encoding: utf-8
"""
@author: donato
@license:
@contact:
@software: tool
@application:
@file: test0.py
@time: 2023/4/4 9:42 AM
@desc:
"""
import re

with open("delete_user.txt", 'r') as f:
# with open("role-resou.log", 'r') as f:
# with open("bj-10.10.14.0.txt", 'r') as f:
    for line in f.readlines():
        lis = re.findall(r"\d{9,12}", line)
        if not lis:
            continue
        # print("".join(lis))
        # print(lis)

        # 删除账号
        print('no localdb account' + " " + '\"' + "".join(lis) + '\"' )


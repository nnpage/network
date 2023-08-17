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

with open("账户.txt", 'r') as f:
    for line in f.readlines():
        lis = re.findall(r"\d{9,12}", line)
        if not lis:
            continue
        # print("".join(lis))
        # print(lis)

        print('localdb update password' + " "  + "".join(lis) +  " " + '\"' + "Aa123456" + '\"')


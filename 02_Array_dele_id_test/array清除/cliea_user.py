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

with open("screen_id.txt", 'r') as f:
    for line in f.readlines():
        print('no localdb group "user_' + line.strip() + '\"')
        print('no role name "role-' + line.strip() + '\"')
        print('no vpn resource group "vpn-' + line.strip() + '\"')
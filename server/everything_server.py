#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('xxx.xxx.xxx.xxx', 9999))
while True:
    data, addr = s.recvfrom(1024)
    filename = data.decode('utf-8')
    os.startfile(filename)

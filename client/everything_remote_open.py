#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import socket

def remote_open_file(filename, host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = bytes(filename.encode('utf-8'))
    s.sendto(data, (host, port))
    s.close()

if __name__ == '__main__':
    host = 'xxx.xxx.xxx.xxx'
    port = 9999

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print(filename)
        remote_open_file(filename, host, port)

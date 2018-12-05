#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
import time
import json
import sys

from functools import partial

from tcp_client import TcpClient
from messages import *
from console_format import console_format

if __name__ == '__main__':
    #agv_ip = '127.0.0.1'
    #agv_ip = '192.168.1.135'
    #agv_ip = '192.168.1.60'
    #agv_ip = '192.168.1.106'
    #agv_ip = '192.168.1.55'
    agv_ip = '192.168.0.3'
    #agv_ip = '192.168.1.162'
    #agv_ip = '192.168.1.173'
    #agv_ip = '192.168.1.161'
    #agv_ip = '192.168.1.151'
    state_client = TcpClient(agv_ip, 8888)
    cmd__ = get_hardware_warn
    


    while(1):
        #print("[ %2d ] sending request..."%i)
        #print(cmd__)
        t_0 = time.time()        
        res__ = state_client.call(cmd__)
        t_1 = time.time()        
        data = json.loads(res__)["data"]

        print res__

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
from api_function import api_function

if __name__ == '__main__':
    agv_ip = '127.0.0.1'
    #agv_ip = '192.168.1.135'
    #agv_ip = '192.168.1.60'
    #agv_ip = '192.168.1.106'
    #agv_ip = '192.168.1.55'
    #agv_ip = '192.168.0.3'
    #agv_ip = '192.168.1.162'
    #agv_ip = '192.168.1.173'
    #agv_ip = '192.168.1.161'
    #agv_ip = '192.168.1.151'


    state_client = TcpClient(agv_ip, 8888)
    cmd__ = get_raw_map

    while(True):
        t_0 = time.time()        
        res__ = state_client.call(get_raw_map)
        #print res__
        t_1 = time.time()        
        res_json = json.loads(res__)
        if("data" not in res_json):
            print res_json
            continue
        data = res_json["data"]

        dt_0 = t_1 - t_0
        
        print("time_diff [  %lf  ]   rate [ % 11.5lf ]    width[ %d ]  height[ %d ]"
              %(dt_0, 1.0/dt_0, data['width'], data['height']))

        break

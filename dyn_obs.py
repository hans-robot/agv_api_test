#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
import time
from functools import partial
import sys
from tcp_client import TcpClient
from messages import *
from api_function import api_function

if __name__ == '__main__':
    #agv_ip = '127.0.0.1'
    #agv_ip = '192.168.1.135'
    #agv_ip = '192.168.1.60'
    #agv_ip = '192.168.1.106'
    #agv_ip = '192.168.1.55'
    agv_ip = '192.168.0.3'
    af = api_function(agv_ip)

    #af.set_output_single([3],"true")

    while(True):
        af.dynamic_obstacle_add('4', 0, 1.0, 0.0, 0.4)
        time.sleep(1)
        af.dynamic_obstacle_del('4')
        time.sleep(1)


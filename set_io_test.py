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
    #agv_ip = '192.168.1.161'
    af = api_function(agv_ip)

    if(True):  
        af.set_output_single([63], 'true')
        time.sleep(3)
        af.set_output_single([63], 'false')
        sys.exit(0) 

    if(False):
        #af.set_output_single([21], 'false') # set outputs one by one
        time.sleep(1)
        af.set_output_single([21], 'true') # set outputs one by one
        #af.set_output_single([1,2,3], 'true') # set outputs one by one
        sys.exit(0)

    i = 0
    j = 1
    k = 2
    while(True):
        af.set_output_single([i+1, j+1, k+1], ['true','false',"false"]) # set outputs one by one
        #af.set_output_single([i+1, j+1, k+1], ['false','false',"false"]) # set outputs one by one
        i = (i+1)%3
        j = (j+1)%3
        k = (k+1)%3
        time.sleep(1)
    #af.play_sound(3,0)

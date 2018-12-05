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

    ##af.enable()
    #af.goFixed(0)
    #af.goMag(1)
    #af.set_idle()
    #af.charge('false')
    af.set_output_single([3],"false")
    time.sleep(1)
    af.set_output_single([3],"true")
    #af.charge('true')
    #af.play_sound(3,0)
    #for i in xrange(3):
    ##    time.sleep(1)

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

    #af.play_sound(3,0)
    #sys.exit(0)    


    af.cancel_task()
    sys.exit(0)

    while(True):
        af.goFixed(10)
        af.goMag(5)

        af.charge('false')
        time.sleep(1)
        af.charge('true')
        af.wait_for_charging()
        af.play_sound(0,0)
        af.play_sound(3,0)
        time.sleep(90)
        af.stop()

        af.goMag(6)

    sys.exit(0)

    while(True):
        af.enable()
        #af.goFixed(0)
        #af.goMag(5)
        af.set_idle()
        af.charge('false')
        time.sleep(1)
        af.charge('true')
        af.play_sound(3,0)
        #for i in xrange(3):
        ##    time.sleep(1)
        af.wait_for_charging()
        time.sleep(3)
        #af.goMag(4)
        #af.goFixed(3)
        af.play_sound(203,0)
        time.sleep(5)

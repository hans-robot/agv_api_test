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
import threading
import math

def loopStateGen(af, keys, data, duration):
    d = data[0]

    loop = [None]

    def loopState():
        for key in keys:
            d[key] = af.getState(key)
        d["get"] = True

    def loopStateOnce():
        for key in keys:
            d[key] = af.getState(key)
        loop[0] = loopState

    loop[0] = loopStateOnce
    
    def loopRet():
        while(d["running"]):
            loop[0]()
            time.sleep(duration)
    
    return loopRet



def angleDiff(a,b):
    pi2 = math.pi * 2
    print a
    print b
    a = a % pi2
    b = b % pi2
    d = a - b
    print a,b
    if (d < 0):
        d += pi2
    if (d > math.pi):
        print pi2, d
        d = pi2 - d
    return d


def rotateFindTape( af, 
                    angle_range = 10/180.0*math.pi, 
                    angular_speed = 0.1,
                    angle_tolerance = 0.01,
                    check_duration = 0.1 ):

    data = [{
        "get": False,
        "running": True,
        "onMagTrack": False,
        "angle": 0
    }]

    t = threading.Thread( target = loopStateGen(af, 
                                                ["onMagTrack", "angle"],
                                                data, 
                                                check_duration) )
    t.setDaemon(True)
    t.start()

    angle_ori = 0.0
    
    #while(not data[0]["onMagTrack"]):
    while(not data[0]["get"]):
        time.sleep(check_duration)

    track_found = False

    if(not data[0]["onMagTrack"]):
        track_found = False
        angle_ori = data[0]["angle"]
        af.switch_manual()

        for dend, dspeed in [[ -1*angle_range, -1 ],
                             [  2*angle_range,  1 ],
                             [ -1*angle_range, -1 ]]:
            af.speed_control( 0, angular_speed * dspeed )
            while( angleDiff(data[0]["angle"], dend) > angle_tolerance ):
                if (data[0]["onMagTrack"]):
                    af.speed_control( 0, 0 )
                    track_found = True
                    break
                    pass # if
                time.sleep(check_duration)
                pass # while
            pass # for

        af.switch_auto()
        pass # if not 
    else:
        track_found = True
        pass # else
        

    #print data[0]["onMagTrack"], data[0]["angle"]

    data[0]["running"] = False
        
    t.join()

    return track_found


if __name__ == '__main__':
    #agv_ip = '127.0.0.1'
    #agv_ip = '192.168.1.135'
    #agv_ip = '192.168.1.60'
    #agv_ip = '192.168.1.106'
    #agv_ip = '192.168.1.55'
    agv_ip = '192.168.0.3'
    af = api_function(agv_ip)

    while(True):
        af.goFixed('32')
        rotateFindTape(af)
        af.goMag(8)
        #time.sleep(1)

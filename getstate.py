#!/usr/bin/env python

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
    cmd__ = get_state
   
    # bool
    once = 0
    # bool
    plot = 0
    # bool
    hide_time = 1


    counter_max = 2000

    t_all = 0.0
    counter = 0

    t_avg = []


    while(1):
        #print("[ %2d ] sending request..."%i)
        #print(cmd__)
        t_0 = time.time()        
        res__ = state_client.call(cmd__)
        t_1 = time.time()        
        data = json.loads(res__)["data"]

        if(1):
            print ("%s\n"
                   "agvState [ %s ]       runningMode [ %s ]    buttonState [ %s ]  isEnable [ %s ]\n" 
                   "controlMode [ %s ]    taskState [ %s ]  taskId [ %s ]\n"
                   "magNode [ %u ]     virtualNode [ %6s ]  onMagTrack [ %s ]\n"
                   "isWheelDown [ %s ]   hasObstacle [ %s ]  obstacleStop [ %s ]  chargeState[ %s ]\n"
                   "battery( power [ %3d ]  voltage [ %5d ]  temperature [ %3d ]  current [ % 6d ])\n"
                   #"currentSpeed [ % .5f ]    x[ % .5f ]    y[ % .5f ]    angle[ % .5f ]\n"
                   "speed [ % .5f ]    x[ % .5f ]    y[ % .5f ]    angle[ % .5f ]\n"
                   #"taskTargetMag [ %11s ]  taskTargetVirtual [ %s ]  taskTargetFreeNode [ %s ]\n"
                   "hardwareWarn[ %s ]\n"
                   "errors [ \n%s ]\n"%(
                       (
                        "\n"+
                        #console_format.CLEAR+
                        "="*20
                       ),
                        data["agvState"], data["runningMode"], data["buttonState"], data["isEnable"], 
                       data["controlMode"], data["taskState"], data["taskId"], 
                       struct.unpack("I",struct.pack("i",data["magNode"]))[0], data["virtualNode"], data["onMagTrack"], 
                       data["isWheelDown"], data["hasObstacle"], data["obstacleStop"], data["chargeState"],
                       data["batteryRemainPower"], data["batteryVoltage"], data["batteryTemperature"], data["batteryCurrent"],
                       data["currentSpeed"], data["x"], data["y"], data["angle"],
                       #data["taskTargetMag"], data["taskTargetVirtual"], data["taskTargetFreeNode"],
                       ' '.join(map(lambda x:"%02X"%x,data["hardwareWarn"])),
                       ''.join(map(lambda x:'   code[ %d ]  message[ %s ]\n'%(x['code'],x['message']),data["errors"]))))

        elif(0):
            print res__
        elif(1):
            print "x[ %s ]   y[ %s ]  a[ %s ]"%(data["x"],
                                                data["y"],
                                                data["angle"])
        else:
            pass

        dt_0 = t_1 - t_0
        t_all += dt_0
        counter += 1

        if(plot):
            t_avg.append([dt_0,t_all/float(counter)])
            if(counter > counter_max):
                break

        if(not hide_time):
            print("[ % 5d ] time_diff [  %lf  ]   % 11.5lf   % 11.5lf"
                  %(counter, dt_0, 1.0/dt_0, t_all/float(counter)))
        time.sleep(0.1)

        if(once):
            break


    if(plot):
        from matplotlib import pyplot as plt
        import numpy as np
        data = np.array(t_avg).T
        dt_, t_avg_ = data[0], data[1]
        #print data
        #print dt_
        #print t_avg_
        plt.plot(dt_, color='red')
        plt.plot(t_avg_, color='blue')
        plt.show()

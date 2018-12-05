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
import math

def format_line(a, lline, fformat, line_num = False):
    l = len(a)
    nstep = l/lline + (1 if l%lline else 0)
    nsteplen = math.log10(nstep) + 1
    res = "\n".join(map( lambda step: " ".join( ["[%%%dd]"%(nsteplen)%step if line_num else ""] + 
                                                map( fformat, 
                                                     a[(step  )*lline: 
                                                       (step+1)*lline] )),
                          xrange(nstep) ))
    return res
        

if __name__ == '__main__':
    #agv_ip = '127.0.0.1'
    #agv_ip = '192.168.1.135'
    #agv_ip = '192.168.1.60'
    #agv_ip = '192.168.1.106'
    #agv_ip = '192.168.1.55'
    agv_ip = '192.168.0.3'
    #agv_ip = '192.168.1.161'
    af = api_function(agv_ip)

    res = af.get_input_single([i for i in xrange(64)])
    res_1 = map( lambda x:1 if x else 0, 
                 res )
    
    print ""
    print format_line( res, 8, lambda x:"% 5s"%x, line_num = True )
    print ""
    print format_line( res_1, 8, lambda x: "%1d"%x, line_num = True )
    sys.exit(0) 

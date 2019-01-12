#!/usr/bin/env python
import socket
import struct
import time
import json
import sys

from functools import partial

from star_tcp_client import StarTcpClient
from star_messages import *
from console_format import console_format


class star_api_function(object):

    __star_port = 10009

    def call(self, client, cmd):
        print cmd
        res = client.call(cmd)
        print res
        return res
    
    def __init__(self,star_ip):
        self.star_ip = star_ip
        self.star_client = StarTcpClient(self.star_ip, self.__star_port)

        self.running = True
        return 

    def play_sound(self, sound_id):
        return self.call( self.star_client, star_agv_play_sound(sound_id) )
        
    def play_sound_time(self, sound_id, keep_seconds=-1):
        self.play_sound(sound_id)
        if(keep_seconds>=0):
            time.sleep(keep_seconds)
        else:
            return
        self.play_sound(0)
        return
        
    def play_sound_repeat(self, sound_id, keep_seconds=-1, repeat_time=-1, play_interval=0):
        if(repeat_time < 0):
            return
        
        self.play_sound_time(sound_id, keep_seconds)
        
        if(keep_seconds <= 0):
            # if < 0, play_sound_time returns immediately, 
            # better not to repeat.
            # if == 0, it doesn't make sense to repeat, too.
            return
        
        for i in xrange(int(repeat_time)):
            if(play_interval > 0):
                time.sleep(play_interval)
            self.play_sound_time(sound_id, keep_seconds)
            
        return
        
            
            
    
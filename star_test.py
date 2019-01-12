#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
import time
from functools import partial
import sys
from star_tcp_client import StarTcpClient
from star_messages import *
from star_api_function import star_api_function
import threading
import math


if __name__ == '__main__':
    #star_ip = '127.0.0.1'
    #star_ip = '192.168.1.135'
    #star_ip = '192.168.1.60'
    #star_ip = '192.168.1.106'
    #star_ip = '192.168.1.55'
    star_ip = '192.168.0.168'
    saf = star_api_function(star_ip)
	
    saf.play_sound_repeat( sound_id = 2,
                           keep_seconds = 2,
                           repeat_time = 2,
                           play_interval = 2 )

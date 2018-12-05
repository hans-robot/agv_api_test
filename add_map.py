#!/usr/bin/env python

import socket
import struct
import time
import json
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

    list_res = af.map_list()
    list_data = json.loads(list_res)["data"]
    map_list = map(lambda x:x.encode('ascii'),list_data["maps"])
    n_map = len(map_list)
    map_now = list_data["currentMap"].encode("ascii")
    map_now_index = map_list.index(map_now)
        
    
    map_now_index += 1
    map_next = map_list[map_now_index%n_map]
    print map_next
    af.change_map(map_next)
    time.sleep(1)

    af.delete_map("zdf_test")
    print af.map_list()
    af.add_map("/home/xlh/Desktop/ZDFmap_3spot.path", "zdf_test")
    af.change_map("zdf_test")

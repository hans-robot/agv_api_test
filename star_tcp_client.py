#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
import time
from functools import partial
import sys

class StarTcpClient(object):
    def __init__(self, ip="localhost", port=8888):
        self.__socket = socket.create_connection((ip, port))

    def close(self):
        self.__socket.shutdown(socket.SHUT_RDWR)
        self.__socket.close()

    def call(self, request):
        """

        :param request:
        :return:
        """
        request_length = len(request)
        #print "!H%ss" % request_length, request, type(request)
        request_bytes = struct.pack("!H%ss" % request_length, request_length, request)
        self.__socket.send(request_bytes)
        response_length_bytes = self.__socket.recv(2)
        response_length = struct.unpack("!H", response_length_bytes)[0]
        #print("length:%s" % response_length)
        acc_len = 0
        response = ""
        while(acc_len < response_length):
            response += self.__socket.recv(response_length)
            acc_len = len(response)
            #print("length:%s" % len(response))
            if "" == response:
                self.close()
                raise RuntimeError("连接中断!sock:" + str(self.__socket.getpeername()))
            return response

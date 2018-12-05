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


class api_function(object):
    def __init__(self,agv_ip):
        self.agv_ip = agv_ip
        self.state_client   = TcpClient(self.agv_ip, 8888)
        self.control_client = TcpClient(self.agv_ip, 8889)
        self.task_client    = TcpClient(self.agv_ip, 8890)
        self.config_client  = TcpClient(self.agv_ip, 8891)

        self.running = True
        return 


    def enable(self):
        self.control_client.call(soft_button('RUN'))
        self.control_client.call(soft_button('RESET'))
        return

    def stop(self):
        self.control_client.call(soft_button('STOP'))
        return

    def switch_auto(self):
        self.control_client.call(change_mode_auto)
        return

    def switch_manual(self):
        self.control_client.call(change_mode_manual)
        return

    def goFree(self,x,y,angle):
        state__ = "IDLE"
        #print(self.task_client.call(cancel_task))

        self.enable()
        self.switch_auto()

        cmd = add_point_task(x,y,angle)
        print cmd
        print(self.task_client.call(cmd))
                 
        while(self.running):
            if(state__ == 'FINISHED'):
                break
            elif(state__ == 'PREEMPTED'):
                pass
                #print(self.task_client.call(cmd))
            else:    
                pass
            res__ =  self.state_client.call(get_state)
            state__ = json.loads(res__)['data']['taskState']
            time.sleep(0.3)
        else:
            print(self.task_client.call(cancel_task))        

        return

    def getState(self, key=""):
        res__ =  self.state_client.call(get_state)
        data = json.loads(res__)['data']
        if(not key):
            return data
        else:
            return data[key]


    def goMag(self,rfid):
        #print(self.task_client.call(cancel_task))
        state__ = "IDLE"

        self.enable()
        self.switch_auto()

        cmd__ = add_mag_task(rfid)
        print(cmd__)
        print(self.task_client.call(cmd__))

        while(self.running):
            res__ =  self.state_client.call(get_state)
            state__ = json.loads(res__)['data']['taskState']
            if(state__ == 'FINISHED'):
                self.task_client.call(cancel_task)
                break
            elif(state__ == 'PREEMPTED'):
                pass
                #print(self.task_client.call(cmd))
            else:
                time.sleep(0.3)
                continue
        else:
            print(self.task_client.call(cancel_task))        

        return


    def goFreeNode(self,node):
        #print(self.task_client.call(cancel_task))
        state__ = "IDLE"

        self.enable()
        self.switch_auto()

        cmd__ = add_target_free_task(node)
        print(cmd__)
        print(self.task_client.call(cmd__))

        while(self.running):
            res__ =  self.state_client.call(get_state)
            state__ = json.loads(res__)['data']['taskState']
            if(state__ == 'FINISHED'):
                self.task_client.call(cancel_task)
                break
            elif(state__ == 'PREEMPTED'):
                pass
                #print(self.task_client.call(cmd))
            else:
                time.sleep(0.3)
                continue
        else:
            print(self.task_client.call(cancel_task))        

        return


    def goFixed(self,node):
        #print(self.task_client.call(cancel_task))
        state__ = "IDLE"

        self.enable()
        self.switch_auto()

        cmd__ = add_target_task(node)
        print(cmd__)
        print(self.task_client.call(cmd__))

        while(self.running):
            res__ =  self.state_client.call(get_state)
            state__ = json.loads(res__)['data']['taskState']
            if(state__ == 'FINISHED'):
                self.task_client.call(cancel_task)
                break
            elif(state__ == 'PREEMPTED'):
                pass
                #print(self.task_client.call(cmd))
            #elif(state__ == 'FAILED'):
            #    self.task_client.call(cmd__)
            #    continue
            else:
                time.sleep(0.3)
                continue
        else:
            print(self.task_client.call(cancel_task))        

        return

    
    def charge(self, start):
        assert start in ['true','false']
        self.enable()
        self.switch_auto()
        
        if(0):
            __cmd = charge('false')
            print __cmd
            print(self.control_client.call(__cmd))
            time.sleep(1)

        __cmd = charge(start)
        print __cmd
        print(self.control_client.call(__cmd))

    # set outputs one by one
    def set_output_single(self, indexes, switches):
        if(isinstance(switches, str)):
            assert switches in ['true','false']
            switches = [switches]*len(indexes)
        for index,switch in zip(indexes, switches):
            print index,switch
            __cmd = set_output(index, switch)
            print __cmd
            print(self.control_client.call(__cmd))


    def get_input_single(self, indexes):
        ret = []
        for index in indexes:
            #print index
            __cmd = get_input(index)
            #print __cmd
            __res = self.state_client.call(__cmd)
            sys.stdout.write("%02d "%index)
            if((index+1)%8==0):
                print ""
            data = json.loads(__res)["data"]
            state = data["state"]
            ret.append(state)
        return ret


    def set_idle(self):
        __cmd = switch_to_idle
        print __cmd
        print(self.task_client.call(__cmd))
    
        
    def play_sound(self, sound_id, repeat_time):
        __cmd = sound(sound_id, repeat_time)
        print __cmd
        print(self.control_client.call(__cmd))

    def wait_for_charging(self):
        cmd__ = get_state
        
        while(True):
            #print("[ %2d ] sending request..."%i)
            print(cmd__)
            res__ = self.state_client.call(cmd__)
            print (res__)
            data = json.loads(res__)["data"]
            if(data["chargeState"] == 'CHARGING'):
                return
            else:
                time.sleep(1)
        
    def map_list(self):
        __cmd = get_map_list
        print __cmd
        __res = self.state_client.call(__cmd)
        print(__res)
        return __res


    def change_map(self, map_name):
        __cmd = change_map(map_name)
        print __cmd
        print(self.config_client.call(__cmd))

    def delete_map(self, map_name):
        __cmd = delete_map(map_name)
        print __cmd
        print(self.config_client.call(__cmd))

    def add_map(self, map_filename, map_name):
        map_data = open(map_filename, "r").read()
        __cmd = add_map(map_name, map_data)
        print __cmd
        print(self.config_client.call(__cmd))

    def cancel_task(self):
        print cancel_task
        print(self.task_client.call(cancel_task))        

    def get_raw_map(self):
        __cmd = get_raw_map
        #print __cmd
        __res = (self.state_client.call(__cmd))
        #print __res
        return __res

    def switch_navigation(self):
        print self.control_client.call(change_map_mode_navigation)
        return

    def switch_mapping(self):
        print self.control_client.call(change_map_mode_mapping)
        return

    def dynamic_obstacle_add(self, name, pose_type, x, y, radius):
        print self.control_client.call(add_dynamic_obstacle(name,
                                                            pose_type,
                                                            x,
                                                            y,
                                                            radius))
        return

    def dynamic_obstacle_del(self, name):
        print self.control_client.call(del_dynamic_obstacle(name))
        return

    def speed_control(self, v, w):
        __cmd = robot_motion(v,0,w)
        __res = self.control_client.call(__cmd)
        print __cmd
        print __res
    

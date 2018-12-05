#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
import time
from functools import partial
import sys
from tcp_client import TcpClient
from messages import *

if __name__ == '__main__':
    #agv_ip = '127.0.0.1'
    #agv_ip = '192.168.1.135'
    #agv_ip = '192.168.1.60'
    #agv_ip = '192.168.1.106'
    #agv_ip = '192.168.1.55'
    agv_ip = '192.168.0.3'
    state_client = TcpClient(agv_ip, 8888)
    control_client = TcpClient(agv_ip, 8889)
    task_client = TcpClient(agv_ip, 8890)
    #config_client = TcpClient(agv_ip, 8891)

    import time
    import json
    
    tori = t = time.time()
    ds = []
    test_count = 100000
    cmd__ = get_state
    #cmd__ = get_map
    #cmd__ = get_input
    # 查询状态
    i = 0
    #print(control_client.call(change_mode_auto))
    #print task_client.call(add_target_free_task(0))

    #res__ = control_client.call(set_output(21,"True"))
    #print res__

    res__ = control_client.call(change_mode_auto)
    print res__


    res__ = task_client.call(add_mag_task(1))
    print res__

    #sys.exit(0)
    while(True):
        #print("[ %2d ] sending request..."%i)
        #print(cmd__)
        res__ = state_client.call(cmd__)
        task_state_ = json.loads(res__)["data"]["taskState"]
        if(task_state_ == "FINISHED"):
            break
        print res__

    res__ = control_client.call(charge("false"))
    print res__
    time.sleep(1)

    res__ = control_client.call(charge("true"))
    print res__

    #while(True):
    #    time.sleep(1)

    sys.exit(0)

    #for i in xrange(test_count):
    while(True):
        #print("[ %2d ] sending request..."%i)
        #print(cmd__)
        res__ = state_client.call(cmd__)
        print res__
        #res__ = control_client.call(sound(i%15))
        #print res__
        #print(json.loads(res__)["data"]["taskState"])
        time.sleep(2)
        t_ = time.time()
        d = t_ - t
        #print "\033[1m%f\033[0m"%(d)
        t = t_
        ds.append(d)
        #print("[ %2d ] OK"%i)
        i+=1

    tend = time.time()
    td = tend-tori
    #print ""
    #print "total time: %f"%(td)

    #print "average time: %f"%(td/float(test_count))
    #from matplotlib import pyplot as plt

    #plt.plot(ds)
    #plt.savefig("test_master_%d_%s.svg"%(test_count, time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())),
    #            format="svg")

    #plt.show()


    #import sys
    #sys.exit(0)

    #control_client.call(set_output(4,"False"))
    #control_client.call(set_output(5,"False"))
    #control_client.call(set_output(6,"False"))
    if(False):
        print "="*10
        print(get_map)
        a = state_client.call(get_map)
        #print(a)
        #print a[45:55]
        import json
        ja = json.loads(a)
        print ja['data']['data']
        print "="*10
      
        foncar = open("xmap_oncar.new.path","w")
        foncar.writelines(ja['data']['data'])
        foncar.close()
   
    if(False): 
        fhere = open('xmap.path','r')
        maphere = fhere.read()
        print maphere
        fhere.close()
        maphere = maphere.replace('\n','\\n').replace('"','\\"')
        print(change_mode_manual)
        print(control_client.call(change_mode_manual))
        print(config_client.call(update_map(maphere)))
   
    import json
    while(False):
        a = [0]*7
	for i in xrange(7):
	    a[i] = 1 if json.loads(state_client.call(get_input(i)))['data']['state'] else 0
        print a


    #print (task_client.call(cancel_task))
    #print (state_client.call(get_laser_scan))
    #print (state_client.call(get_area)) 
    # "x":2.214648,"y":-2.2297666,"angle":-1.1854893
    #print(control_client.call(robot_reloc(2.21468,-2.229766,-1.1854893)))
    print(control_client.call(change_mode_auto))
    print(control_client.call(soft_button('RUN')))
    #print(task_client.call(cancel_task))
    #print(task_client.call(add_point_task(2.21468,-2.229766,-1.1854893)))
    #while(True):
    #	time.sleep(1)
    print(state_client.call(get_state))
    #print(state_client.call(get_map))
    print(state_client.call(get_area))

    #control_client.call(set_output(4,"True"))
    #control_client.call(set_output(5,"True"))
    #control_client.call(set_output(6,"True"))
    #time.sleep(2)

    #control_client.call(set_output(1,"True"))

    #control_client.call(set_output(1,"True"))

    import signal

    running = True

    ok = True


    def shutdown_hd(a,b):
        running = False
        print "SHUTDOWN( %s, %s )"%(a,b)
        print(task_client.call(cancel_task))        
        control_client.call(set_output(5,"False"))



    #signal.signal(signal.SIGINT, shutdown_hd)
    #print(cancel_task)        
    #print(task_client.call(cancel_task))        

    import json

    rot_ok = False
    def rotate_angle(a):
        global running
        global rot_ok
        rot_ok = True
        res__ =  state_client.call(get_state)
        ori_angle__ = float(json.loads(res__)['data']['angle'])
        while(running):
            if(not rot_ok):
                res__ =  state_client.call(get_state)
                angle__ = float(json.loads(res__)['data']['angle'])
                diff__ = angle__-ori_angle__
                if(diff__ < 0):
                    diff__ += (3.1415926535*2.0)
                if(diff__ >= a):
                    rot_ok = True
                    control_client.call(robot_motion(0,0,0))
                    break
                else:
                    continue
            else:
                rot_ok = False
                cmd__ = robot_motion(0,0,0.3)
                print(cmd__)
                print(control_client.call(cmd__))
            time.sleep(0.5)
        else:
            print(control_client.call(robot_motion(0,0,0)))        



    def rotate_to_mag():
        global running
        global rot_ok
        rot_ok = True
        res__ =  state_client.call(get_state)
        online__ = json.loads(res__)['data']['onMagTrack']
        if(online__):
            return
        while(running):
            if(not rot_ok):
                res__ =  state_client.call(get_state)
                online__ = json.loads(res__)['data']['onMagTrack']
                if(online__):
                    rot_ok = True
                    control_client.call(robot_motion(0,0,0))
                    break
                else:
                    continue
            else:
                rot_ok = False
                cmd__ = robot_motion(0,0,0.3)
                print(cmd__)
                print(control_client.call(cmd__))
            time.sleep(0.5)
        else:
            print(control_client.call(robot_motion(0,0,0)))        
            


    def rotate_back_to_track():
        global running
        if(running):
            rotate_angle(3.14159265/2.0)
        if(running):
            rotate_to_mag()
            
            
    def looping():
        global running
        global ok
        control_client.call(change_mode_auto)
        l = [1,2]
        m = [2,2] #[2,4]
        #m = [4,2]
        i = 0
        while(running):
            if(not ok):
                res__ =  state_client.call(get_state)
                state__ = json.loads(res__)['data']['taskState']
                if(state__ == 'FINISHED'):
                    ok = True

                    task_client.call(cancel_task)
                    time.sleep(3)

                    print "\033[1;33m OK!!!! HORRAY!!!!\033[0m"
                    #control_client.call(change_mode_manual)
                    #rotate_back_to_track()
                else:
                    continue
            else:
                ok = False
                ###cmd__ = add_target_task(l[i])
                #control_client.call(change_mode_auto)
                control_client.call(soft_button('STOP'))
                ##task_client.call(cancel_task)
                #cmd__ = add_mag_task(m[i])
                time.sleep(3)
                control_client.call(soft_button('RUN'))
                i = 1-i
                print(cmd__)
                print(task_client.call(cmd__))
            #time.sleep(0.5)
        else:
            print(task_client.call(cancel_task))        

    import threading
    #tloop = threading.Thread(target=looping)
    #tloop.setDaemon(True)
    #tloop.start()
    #looping()
    
    #control_client.call(set_output(5,"True"))
     
    print(change_mode_auto)    
    print(control_client.call(change_mode_auto))

    if False:
        state__ = "FINISHED"
        import json
        l = [0,2]
        i = 0
        while(running):
            if(state__ == 'FINISHED'):
                print add_target_task(l[i])
                print "\033[1;33m=========\033[0m"
                print(task_client.call(add_target_task(l[i])))
                i = 1-i
            else:    
                pass
            res__ =  state_client.call(get_state)
            state__ = json.loads(res__)['data']['taskState']
            time.sleep(2)

    def goFixed(nid):
        state__ = "IDLE"
        global control_client
        global change_mode_auto
        global state_client
        global get_state
        global soft_button
        global cancel_task
        global task_client
        #print(task_client.call(cancel_task))

        control_client.call(change_mode_auto)
        control_client.call(soft_button('RUN'))
        global running
        import json
        cmd = add_target_task(nid)
        print cmd
        print(task_client.call(cmd))
                
        while(running):
            if(state__ == 'FINISHED'):
                break
            else:    
                pass
            res__ =  state_client.call(get_state)
            state__ = json.loads(res__)['data']['taskState']
            time.sleep(0.3)
        else:
            print(task_client.call(cancel_task))

    def goFree(x,y,angle):
        state__ = "IDLE"
        global control_client
        global change_mode_auto
        global state_client
        global get_state
        global soft_button
        global cancel_task
        global task_client
        control_client.call(change_mode_auto)
        control_client.call(soft_button('RUN'))
        global running
        import json
        #print(task_client.call(cancel_task))

        cmd = add_point_task(x,y,angle)
        print cmd
        print(task_client.call(cmd))
                 
        while(running):
            if(state__ == 'FINISHED'):
                break
            elif(state__ == 'PREEMPTED'):
                pass
                #print(task_client.call(cmd))
            else:    
                pass
            res__ =  state_client.call(get_state)
            state__ = json.loads(res__)['data']['taskState']
            time.sleep(0.3)
        else:
            print(task_client.call(cancel_task))        



    def goMag(rfid):
        global running
        global control_client
        global change_mode_auto
        global state_client
        global get_state
        global cancel_task
        global soft_button
        global task_client
        print(task_client.call(cancel_task))

        control_client.call(change_mode_auto)
        control_client.call(soft_button('RUN'))

        cmd__ = add_mag_task(rfid)
        print(cmd__)
        print(task_client.call(cmd__))

        while(running):
            res__ =  state_client.call(get_state)
            state__ = json.loads(res__)['data']['taskState']
            if(state__ == 'FINISHED'):
                task_client.call(cancel_task)
                break
            else:
                time.sleep(1)
                continue
        else:
            print(task_client.call(cancel_task))        


    while(True):
        goFree(2.9650000441819429,1.3800000205636023,-1.6949859857559204)
        goFixed(2)
        goMag(2)
        goFree(3.1700000472366807,3.5900000534951686,1.5085607767105103)
        goFixed(4)
        goMag(4)

    #print(task_client.call(cancel_task))        

    if False:
        for i in [1,2,3]:
            control_client.call(set_output(i,"True"))
            sleep(0.3)
            control_client.call(set_output(i,"False"))


    if(False):
        led_out = [4,5,6]
        for i in xrange(9):
            cmd__ = set_output(led_out[i%3-1],"False")
            print cmd__
            print(control_client.call(cmd__))
            cmd__ = set_output(led_out[i%3],"True")
            print cmd__
            print(control_client.call(cmd__))
            time.sleep(0.1)

    #control_client.call(set_output(4,"True"))
    #control_client.call(set_output(5,"True"))
    #control_client.call(set_output(6,"True"))
    #time.sleep(0.5)

    #control_client.call(set_output(4,"False"))
    #control_client.call(set_output(5,"False"))
    #control_client.call(set_output(6,"False"))


    #i = sound(1)
    #print(i)
    #print(control_client.call(i))
    #time.sleep(1)
    
    #i = sound(0)
    #print(i)
    #print(control_client.call(i))

    #切换模式
    #print(control_client.call(change_mode_auto))
    #print(state_client.call(get_state))

    #print(task_client.call(cancel_task))

    #print(add_target_task(2))
    #print(task_client.call(add_target_task(2)))

    """
    #到点任务
    print(task_client.call(add_point_task))

    time.sleep(3)

    print(task_client.call(cancel_task))

    #切换模式到手动
    print(control_client.call(change_mode_manual))
    print (control_client.call(robot_motion))
    time.sleep(13)

    #点到点
    print (task_client.call(add_target_task))
    """



#!/usr/bin/env python
del_dynamic_obstacle = lambda name: '''
    {
        "method": "DeleteDynamicObstacle",
        "params": {
            "obstacleName": "%s"
        },
        "id": "100"
    }'''%(name)

add_dynamic_obstacle = lambda name, pose_type, x, y, r: '''
    {
        "method": "AddDynamicObstacle",
        "params": {
            "obstacleName": "%s",
            "poseType": %d,
            "x": %lf,
            "y": %lf,
            "radius": %lf
        },
        "id": "100"
    }'''%(name, pose_type, x, y, r)

add_target_task = lambda i:'''
    {
        "method": "AddTargetTask",
        "params": {
            "taskId": 1,
            "target": "%s"
        },
        "id": "100"
    }'''%i

add_target_free_task = lambda i:'''
    {
        "method": "AddTargetFreeTask",
        "params": {
            "taskId": 1,
            "target": "%s"
        },
        "id": "100"
    }'''%i

add_mag_task = lambda i:'''
    {
        "method": "AddMagTask",
        "params": {
            "taskId": 1,
            "target": "%d"
        },
        "id": "100"
    }'''%i

robot_reloc = lambda x,y,angle:'''
    {
        "method": "RobotReloc",
        "params": {
            "x": %f,
            "y": %f,
            "angle": %f
        },
        "id": "100"
    }'''%(x,y,angle)


add_point_task = lambda x,y,angle:'''
    {
        "method": "AddPointTask",
        "params": {
            "taskId": 2,
            "x": %f,
            "y": %f,
            "angle": %f
        },
        "id": "100"
    }'''%(x,y,angle)
get_state = '''
    {
        "id": "100",
        "method": "GetState",
        "params": {
        }
    }'''
get_map = '''
    {
        "id": "100",
        "method": "GetMap",
        "params": {
        }
    }'''
get_map_list = '''
    {
        "id": "100",
        "method": "GetMapList",
        "params": {
        }
    }'''
get_input = lambda i:'''
    {
        "id": "100",
        "method": "GetInput",
        "params": {
             "index":%d
        }
    }'''%i
sound = lambda i,j:'''
    {
        "id": "100",
        "method": "PlaySound",
        "params": {
             "soundId":%d,
             "repeat_time":%d
        }
    }'''%(i,j)

get_laser_scan = '''
    {
        "id": "100",
        "method": "GetLaserScan",
        "params": {
        }
    }'''
get_area = '''
    {
        "id": "100",
        "method": "GetArea",
        "params": {
        }
    }'''
cancel_task = '''
    {
        "method": "CancelTask",
        "params": {
        },
        "id": "100"
    }'''
change_mode_auto = '''
    {
        "method": "ChangeMode",
        "params": {
            "mode":"AUTO"
        },
        "id": "100"
    }'''

change_mode_manual = '''
    {
        "method": "ChangeMode",
        "params": {
            "mode":"MANUAL"
        },
        "id": "100"
    }''' 

robot_motion = lambda vx,vy,vw:'''
    {
        "method": "RobotMotion",
        "params": {
            "vx":%f,
            "vy":%f,
            "vw":%f
        },
        "id": "100"
    }'''%(vx,vy,vw)
set_output = lambda i,s:'''
    {
        "method": "SetOutput",
        "params": {
            "index":%s,
            "state":\"%s\"
        },
        "id": "100"
    }'''%(i,s)
soft_button = lambda i:'''
    {
        "method": "TriggerSoftButton",
        "params": {
            "softButton":"%s"
        },
        "id": "100"
    }
    '''%(i)
charge = lambda x:'''
    {
        "method": "Charge",
        "params": {
            "start":%s
        },
        "id": "100"
    }
    '''%x

update_map = lambda m:'''
    {
        "method": "UpdateMap",
        "params": {
            "mapData":"%s"
        },
        "id": "100"
    }
    '''%m
    
switch_to_idle = '''
    {
        "method": "SwitchToIdle",
        "params": {
        },
        "id": "100"
    }
    '''

get_hardware_warn = '''
    {
        "id": "100",
        "method": "GetHardwareWarn",
        "params": {
        }
    }'''
change_map = lambda m:'''
    {
        "method": "ChangeMap",
        "params": {
            "map_name":"%s"
        },
        "id": "100"
    }
    '''%m

delete_map = lambda m:'''
    {
        "method": "DeleteMap",
        "params": {
            "map_name":"%s"
        },
        "id": "100"
    }
    '''%m

add_map = lambda name,data:'''
    {
        "method": "AddMap",
        "params": {
            "map_name":"%s",
            "map_data":"%s"
        },
        "id": "100"
    }
    '''%(name,data.replace("\"","\\\"").replace("\n",""))

get_raw_map = '''
    {
        "id": "100",
        "method": "GetRawMap",
        "params": {
        }
    }'''

change_map_mode_navigation = '''
    {
        "method": "ChangeMapMode",
        "params": {
            "mode":"NAVIGATION"
        },
        "id": "100"
    }'''

change_map_mode_mapping = '''
    {
        "method": "ChangeMapMode",
        "params": {
            "mode":"MAPPING"
        },
        "id": "100"
    }'''

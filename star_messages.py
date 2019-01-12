def star_agv_play_sound(index, id=100):
    return '''
{ 
    "method": "StarAgvPlaySound", 
    "id": "%d",
    "params": {  
        "index":%d
    }  
}
'''%(id,index)

def star_agv_get_state(id=100): 
    return '''
{ 
    "method": "StarAgvGetState", 
    "id": "%d",
    "params": {  
    }  
} 
'''%(id)

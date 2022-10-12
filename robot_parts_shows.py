def upper_body(self, robot_parts: dict):
    if robot_parts["head"]["is_available"] and robot_parts["head_gun"]["is_available"]:
        return fr""""
         0: {robot_parts["head"]["name"]}
         Is available: {robot_parts["head"]["is_available"]}
         Attack: {robot_parts["head"]["attack"]}                              
         Defense: {robot_parts["head"]["defense"]}
         Energy consumption: {robot_parts["head"]["energy_consumption"]}
                  ^
                  |                  |1: {robot_parts["head_gun"]["name"]}
                  |                  |Is available: {robot_parts["head_gun"]["is_available"]}
         ____     |    ____          |Attack: {robot_parts["head_gun"]["attack"]}
        |oooo|  ____  |oooo| ------> |Defense: {robot_parts["head_gun"]["defense"]}
        |oooo| '    ' |oooo|         |Energy consumption: {robot_parts["head_gun"]["energy_consumption"]}
        |oooo|/\_||_/\|oooo|"""

    elif not robot_parts["head"]["is_available"]:
        return fr""""         
                                     |1: {robot_parts["head_gun"]["name"]}
                                     |Is available: {robot_parts["head_gun"]["is_available"]}
         ____          ____          |Attack: {robot_parts["head_gun"]["attack"]}
        |oooo|        |oooo| ------> |Defense: {robot_parts["head_gun"]["defense"]}
        |oooo|        |oooo|         |Energy consumption: {robot_parts["head_gun"]["energy_consumption"]}
        |oooo|        |oooo|"""

    elif not robot_parts["head_gun"]["is_available"]:
        return fr""""
         0: {robot_parts["head"]["name"]}
         Is available: {robot_parts["head"]["is_available"]}
         Attack: {robot_parts["head"]["attack"]}                              
         Defense: {robot_parts["head"]["defense"]}
         Energy consumption: {robot_parts["head"]["energy_consumption"]}
                  ^
                  |                  
                  |                  
                  |                  
                ____          
               '    '                
              /\_||_/\      """
    else:
        return ""
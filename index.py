class RobotsWar:
    colors = {
        "black": '\x1b[90m',
        "blue": '\x1b[94m',
        "cyan": '\x1b[96m',
        "green": '\x1b[92m',
        "magenta": '\x1b[95m',
        "red": '\x1b[91m',
        "white": '\x1b[97m',
        "yellow": '\x1b[93m',
    }

    round_player = 1

    # To set initial configurations
    def __init__(self, name_robot_1: str, name_robot_2: str, color_robot_1: str = "blue", color_robot_2: str = "red"):
        def make_part_configurations(name: str, attack: int, defense: int, energy_consumption: int):
            return {
                "name": name,
                "is_available": True,
                "attack": attack,
                "defense": defense,
                "energy_consumption": energy_consumption,
            }

        self.parts = {
            "head": make_part_configurations(name="Head", attack=10, defense=20, energy_consumption=5),
            "head_gun": make_part_configurations(name="Missile Launcher", attack=30, defense=20, energy_consumption=30),
            "left_arm": make_part_configurations(name="Left Arm", attack=5, defense=25, energy_consumption=10),
            "right_arm": make_part_configurations(name="Right Arm", attack=5, defense=25, energy_consumption=10),
            "left_leg": make_part_configurations(name="Left Leg", attack=10, defense=20, energy_consumption=15),
            "right_leg": make_part_configurations(name="Right Leg", attack=10, defense=20, energy_consumption=20)
        }

        global_robots_configurations = {
            "parts": self.parts,
            "energy": 100
        }

        self.robot_1 = {
            "name": name_robot_1,
            **global_robots_configurations
        }

        self.robot_2 = {
            "name": name_robot_2,
            **global_robots_configurations
        }

        self.show_robot(self.robot_1["parts"], "blue")

    @staticmethod
    def is_available_part(part_name: str, player_parts: dict) -> bool:
        return player_parts[part_name]["is_available"]
        
    @staticmethod
    def is_robot_dead(robot: dict):
        return robot["energy"] <= 0

    def show_energy(self, robot: dict):
        energy = robot["energy"]

        color: str

        if energy >= 90:
            color = self.colors["green"]
        elif 40 <= energy < 90:
            color = self.colors["yellow"]
        else:
            color = self.colors["red"]
            print(self.colors["yellow"] + "A L E R T!".center(20))

        print(color + "-"*20)
        print(color + f"{energy} of energy".center(20))
        print(color + "-"*20)

    def show_robot(self, robot_parts: dict, color: str):
        print(self.colors[color] +
              select_upper_body(robot_parts) +
              select_body(robot_parts) +
              select_bottom_body(robot_parts))


# this method select the component of robot to show if is available
def select_upper_body(robot_parts: dict):
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

    elif not robot_parts["head"]["is_available"] and robot_parts["head_gun"]["is_available"]:
        return fr""""         
                                         |1: {robot_parts["head_gun"]["name"]}
                                         |Is available: {robot_parts["head_gun"]["is_available"]}
             ____          ____          |Attack: {robot_parts["head_gun"]["attack"]}
            |oooo|        |oooo| ------> |Defense: {robot_parts["head_gun"]["defense"]}
            |oooo|        |oooo|         |Energy consumption: {robot_parts["head_gun"]["energy_consumption"]}
            |oooo|        |oooo|"""

    elif not robot_parts["head_gun"]["is_available"] and robot_parts["head"]["is_available"]:
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
        return """


        """


def select_body(robot_parts: dict):
    if robot_parts["left_arm"]["is_available"] and robot_parts["right_arm"]["is_available"]:
        return rf"""
            `----' / __ \  `----'           |2: {robot_parts["left_arm"]["name"]}
           '/  |#|/\/__\/\|#|  \'           |Is available: {robot_parts["left_arm"]["is_available"]}
           /  \|#|| |/\| ||#|/  \           |Attack: {robot_parts["left_arm"]["attack"]}
          / \_/|_|| |/\| ||_|\_/ \          |Defense: {robot_parts["left_arm"]["defense"]}
         |_\/    O\=----=/O    \/_|         |Energy consumption: {robot_parts["left_arm"]["energy_consumption"]}
         <_>      |=\__/=|      <_> ------> |
         <_>      |------|      <_>         |3: {robot_parts["right_arm"]["name"]}
         | |   ___|======|___   | |         |Is available: {robot_parts["right_arm"]["is_available"]}
        // \\ / |O|======|O| \  //\\        |Attack: {robot_parts["right_arm"]["attack"]}
        |  |  | |O+------+O| |  |  |        |Defense: {robot_parts["right_arm"]["defense"]}
        |\/|  \_+/        \+_/  |\/|        |Energy consumption: {robot_parts["right_arm"]["energy_consumption"]}
        \__/  _|||        |||_  \__/        """

    elif not robot_parts["left_arm"]["is_available"] and robot_parts["right_arm"]["is_available"]:
        return rf"""
            `----' / __ \  `----'           
               |#|/\/__\/\|#|  \'           
               |#|| |/\| ||#|/  \           
               |_|| |/\| ||_|\_/ \          |3: {robot_parts["right_arm"]["name"]}
                 O\=----=/O    \/_|         |Is available: {robot_parts["right_arm"]["is_available"]}
                  |=\__/=|      <_> ------> |Attack: {robot_parts["right_arm"]["attack"]}
                  |------|      <_>         |Defense: {robot_parts["right_arm"]["defense"]}
               ___|======|___   | |         |Energy consumption: {robot_parts["right_arm"]["energy_consumption"]}
              / |O|======|O| \  //\\        
              | |O+------+O| |  |  |        
              \_+/        \+_/  |\/|        
              _|||        |||_  \__/        """
    elif robot_parts["left_arm"]["is_available"] and not robot_parts["right_arm"]["is_available"]:
        return rf"""
            `----' / __ \  `----'           
           '/  |#|/\/__\/\|#|               
           /  \|#|| |/\| ||#|               
          / \_/|_|| |/\| ||_|               |2: {robot_parts["left_arm"]["name"]}
         |_\/    O\=----=/O                 |Is available: {robot_parts["left_arm"]["is_available"]}
         <_>      |=\__/=|          ------> |Attack: {robot_parts["left_arm"]["attack"]}
         <_>      |------|                  |Defense: {robot_parts["left_arm"]["defense"]}
         | |   ___|======|___               |Energy consumption: {robot_parts["left_arm"]["energy_consumption"]}
        // \\ / |O|======|O| \              
        |  |  | |O+------+O| |              
        |\/|  \_+/        \+_/              
        \__/  _|||        |||_              """
    else:
        return rf"""
            `----' / __ \  `----'           
               |#|/\/__\/\|#|               
               |#|| |/\| ||#|               
               |_|| |/\| ||_|               
                 O\=----=/O                 
                  |=\__/=|           
                  |------|                  
               ___|======|___               
              / |O|======|O| \              
              | |O+------+O| |              
              \_+/        \+_/              
              _|||        |||_              """


def select_bottom_body(robot_parts: dict):
    print(robot_parts)
    if robot_parts["left_leg"]["is_available"] and robot_parts["right_leg"]["is_available"]:
        return rf"""
              | ||        || |          |4: {robot_parts["left_leg"]["name"]} 
             [==|]        [|==]         |Is available: {robot_parts["left_leg"]["is_available"]}
             [===]        [===]         |Attack: {robot_parts["left_leg"]["attack"]}
              >_<          >_<          |Defense: {robot_parts["left_leg"]["defense"]}
             || ||        || ||         |Energy consumption: {robot_parts["left_leg"]["energy_consumption"]}
             || ||        || || ------> |
             || ||        || ||         |5: {robot_parts["right_leg"]["name"]}
           __|\_/|__    __|\_/|__       |Is available: {robot_parts["right_leg"]["is_available"]}
          /___n_n___\  /___n_n___\      |Attack: {robot_parts["right_leg"]["attack"]}
                                        |Defense: {robot_parts["right_leg"]["defense"]}
                                        |Energy consumption: {robot_parts["right_leg"]["energy_consumption"]}
        """
    elif not robot_parts["left_leg"]["is_available"] and robot_parts["right_leg"]["is_available"]:
        return rf"""
                          || |           
                          [|==]         
                          [===]         
                           >_<          |5: {robot_parts["right_leg"]["name"]}
                          || ||         |Is available: {robot_parts["right_leg"]["is_available"]}
                          || || ------> |Attack: {robot_parts["right_leg"]["attack"]}
                          || ||         |Defense: {robot_parts["right_leg"]["defense"]}
                        __|\_/|__       |Energy consumption: {robot_parts["right_leg"]["energy_consumption"]}
                       /___n_n___\      
                                        
                                        
        """
    elif robot_parts["left_leg"]["is_available"] and not robot_parts["right_leg"]["is_available"]:
        return rf"""
              | ||                       
             [==|]                      
             [===]                      
              >_<                       |5: {robot_parts["left_leg"]["name"]}
             || ||                      |Is available: {robot_parts["left_leg"]["is_available"]}
             || ||              ------> |Attack: {robot_parts["left_leg"]["attack"]}
             || ||                      |Defense: {robot_parts["left_leg"]["defense"]}
           __|\_/|__                    |Energy consumption: {robot_parts["left_leg"]["energy_consumption"]}
          /___n_n___\                   
                                        
                                        
        """
    return "\n\n"
RobotsWar("Willian", "Junin")

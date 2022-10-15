# this method select the component of robot to show if is available

def select_upper_body(robot_parts: dict):
    if robot_parts["head_status"] and robot_parts["weapon_status"]:
        return r"""
             0: {head_name}
             Is available: {head_status}
             Attack: {head_attack}                              
             Defense: {head_defense}
             Energy consumption: {head_energy_consump}
                      ^
                      |                  |1: {weapon_name}
                      |                  |Is available: {weapon_status}
             ____     |    ____          |Attack: {weapon_attack}
            |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
            |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consump}
            |oooo|/\_||_/\|oooo|"""

    elif not robot_parts["head_status"] and robot_parts["weapon_status"]:
        return r"""         
                                         |1: {weapon_name}
                                         |Is available: {weapon_status}
             ____          ____          |Attack: {weapon_attack}
            |oooo|        |oooo| ------> |Defense: {weapon_defense}
            |oooo|        |oooo|         |Energy consumption: {weapon_energy_consump}
            |oooo|        |oooo|"""

    elif not robot_parts["weapon_status"] and robot_parts["head_status"]:
        return r"""
             0: {head_name}
             Is available: {head_status}
             Attack: {head_attack}                              
             Defense: {head_defense}
             Energy consumption: {head_energy_consump}
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
    if robot_parts["left_arm_status"] and robot_parts["right_arm_status"]:
        return r"""
            `----' / __ \  `----'           |2: {left_arm_name}
           '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
           /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
          / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
         |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
         <_>      |=\__/=|      <_> ------> |
         <_>      |------|      <_>         |3: {right_arm_name}
         | |   ___|======|___   | |         |Is available: {right_arm_status}
        // \\ / |O|======|O| \  //\\        |Attack: {right_arm_attack}
        |  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
        |\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
        \__/  _|||        |||_  \__/        """

    elif not robot_parts["left_arm_status"] and robot_parts["right_arm_status"]:
        return r"""
            `----' / __ \  `----'           
               |#|/\/__\/\|#|  \'           
               |#|| |/\| ||#|/  \           
               |_|| |/\| ||_|\_/ \          |3: {right_arm_name}
                 O\=----=/O    \/_|         |Is available: {right_arm_status}
                  |=\__/=|      <_> ------> |Attack: {right_arm_attack}
                  |------|      <_>         |Defense: {right_arm_defense}
               ___|======|___   | |         |Energy consumption: {right_arm_energy_consump}
              / |O|======|O| \  //\\        
              | |O+------+O| |  |  |        
              \_+/        \+_/  |\/|        
              _|||        |||_  \__/        """
    elif robot_parts["left_arm_status"] and not robot_parts["right_arm_status"]:
        return r"""
            `----' / __ \  `----'           
           '/  |#|/\/__\/\|#|               
           /  \|#|| |/\| ||#|               
          / \_/|_|| |/\| ||_|               |2: {left_arm_name}
         |_\/    O\=----=/O                 |Is available: {left_arm_status}
         <_>      |=\__/=|          ------> |Attack: {left_arm_attack}
         <_>      |------|                  |Defense: {left_arm_defense}
         | |   ___|======|___               |Energy consumption: {left_arm_energy_consump}
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
    if robot_parts["left_leg_status"] and robot_parts["right_leg_status"]:
        return r"""
              | ||        || |          |4: {left_leg_name} 
             [==|]        [|==]         |Is available: {left_leg_status}
             [===]        [===]         |Attack: {left_leg_attack}
              >_<          >_<          |Defense: {left_leg_defense}
             || ||        || ||         |Energy consumption: {left_leg_energy_consump}
             || ||        || || ------> |
             || ||        || ||         |5: {right_leg_name}
           __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
          /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                        |Defense: {right_leg_defense}
                                        |Energy consumption: {right_leg_energy_consump}
        """
    elif not robot_parts["left_leg_status"] and robot_parts["right_leg_status"]:
        return r"""
                          || |           
                          [|==]         
                          [===]         
                           >_<          |5: {right_leg_name}
                          || ||         |Is available: {right_leg_status}
                          || || ------> |Attack: {right_leg_attack}
                          || ||         |Defense: {right_leg_defense}
                        __|\_/|__       |Energy consumption: {right_leg_energy_consump}
                       /___n_n___\      


        """
    elif robot_parts["left_leg_status"] and not robot_parts["right_leg_status"]:
        return r"""
              | ||                       
             [==|]                      
             [===]                      
              >_<                       |4: {left_leg_name}
             || ||                      |Is available: {left_leg_status}
             || ||              ------> |Attack: {left_leg_attack}
             || ||                      |Defense: {left_leg_defense}
           __|\_/|__                    |Energy consumption: {left_leg_energy_consump}
          /___n_n___\                   


        """
    return "\n\n"


class Parts:
    def __init__(self, name: str, attack: int, defense: int, energy_consumption: int, selector: str):
        self.name = name
        self.is_available = True
        self.attack = attack
        self.defense = defense
        self.energy_consumption = energy_consumption
        self.selector = selector

    def get_status_dict(self):
        return {
            f"{self.selector}_name": self.name.capitalize().strip(),
            f"{self.selector}_status": self.is_available,
            f"{self.selector}_attack": self.attack,
            f"{self.selector}_defense": self.defense,
            f"{self.selector}_energy_consump": self.energy_consumption,
        }

    def set_status(self, status: bool):
        self.is_available = status

    def decrease_defense(self, decrease: int):
        self.defense -= decrease


class Robot:
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
    def __init__(self, name_player: str, name_robot: str, robot_color: str = "blue"):
        self.parts = {
            "head": Parts(name="Head", attack=10, defense=20, energy_consumption=5, selector="head"),
            "weapon": Parts(name="Missile Launcher", attack=30, defense=20, energy_consumption=30, selector="weapon"),
            "left_arm": Parts(name="Left Arm", attack=5, defense=25, energy_consumption=10, selector="left_arm"),
            "right_arm": Parts(name="Right Arm", attack=5, defense=25, energy_consumption=10, selector="right_arm"),
            "left_leg": Parts(name="Left Leg", attack=10, defense=20, energy_consumption=15, selector="left_leg"),
            "right_leg": Parts(name="Right Leg", attack=10, defense=20, energy_consumption=20, selector="right_leg")
        }

        self.player = {
            "name": name_player
        }

        self.robot = {
            "name": name_robot,
            "parts": self.parts,
            "energy": 100,
            "color": robot_color
        }

        self.robot["parts"]["weapon"].set_status(False)

    def say_hi(self):
        print(f"hello, i'm {self.robot['name']} and my boss is {self.player['name']}")

    def is_available_part(self, part_name: str) -> bool:
        return self.robot["parts"][part_name].is_available
        
    def is_on(self):
        return self.robot["energy"] <= 0

    def show_energy(self):
        energy = self.robot["energy"]

        color: str

        if energy >= 70:
            color = self.colors["green"]
        elif 40 <= energy < 70:
            color = self.colors["yellow"]
        else:
            color = self.colors["red"]
            print(self.colors["yellow"] + "A L E R T!".center(65))

        print(color + "="*65)
        print(color + f"{energy}% of energy".center(65))
        print(color + "="*65 + "\x1b[m")

    def get_all_parts(self):
        all_parts = {}

        for i in self.parts.values():
            all_parts.update(i.get_status_dict())

        return all_parts

    def show_robot(self):
        all_parts = self.get_all_parts()
        print((self.colors[self.robot["color"]] +
              select_upper_body(all_parts) +
              select_body(all_parts) +
              select_bottom_body(all_parts) + "\x1b[m").format(**all_parts))

    def decrease_energy(self, decrease: int):
        self.robot["energy"] -= decrease

    def decrease_part_defense(self, part, decrease):
        self.robot["parts"][part.lower().strip()].decrease_defense(decrease)


a = Robot(name_player="Willian", name_robot="Jubscleuson", robot_color="red")

a.decrease_energy(20)
a.decrease_part_defense("head", 10)
a.show_robot()
a.show_energy()
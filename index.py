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
        if self.defense <= 0:
            self.is_available = False

    def get_attack(self):
        return self.attack


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

    stop_color = '\x1b[m'

    colors_options = {}

    # To set initial configurations
    def __init__(self, name_player: str, robot_name: str, default_robot_color: str = "blue") -> object:
        for index, color in enumerate(self.colors):
            self.colors_options[index + 1] = color

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
            "name": robot_name,
            "parts": self.parts,
            "energy": 100,
            "color": default_robot_color
        }

        self.robot["parts"]["weapon"].set_status(False)

    def say_hi(self):
        print(f"\nhello, i'm {self.robot['name']} and my boss is {self.player['name']}")

    def is_available_part(self, part_name: str) -> bool:
        return self.robot["parts"][part_name].is_available
        
    def is_on(self) -> bool:
        return self.robot["energy"] <= 0

    def show_energy(self) -> None:
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
        print(f"{energy}% of energy".center(65))
        print("="*65 + self.stop_color)

    def get_all_parts(self) -> dict:
        all_parts = {}

        for i in self.parts.values():
            all_parts.update(i.get_status_dict())

        return all_parts

    def show_robot(self):
        all_parts = self.get_all_parts()
        print((self.colors[self.robot["color"]] +
              select_upper_body(all_parts) +
              select_body(all_parts) +
              select_bottom_body(all_parts) + self.stop_color).format(**all_parts))

    def decrease_energy(self, decrease: int):
        self.robot["energy"] -= decrease

    def decrease_part_defense(self, part: str, decrease: int):
        part_formatted = part.lower().strip()
        self.robot["parts"][part_formatted].decrease_defense(decrease)

    def show_color_options(self):
        message = f"\n\nAVAILABLE COLORS\n{'-'*16}\n"

        colors_options_values = self.colors_options.values()
        for index, color in enumerate(colors_options_values):
            message += f"{index + 1} : {self.colors[color]}{color.capitalize()}{self.stop_color}\n"

        print(message)

    def set_color(self, color_number: int):
        if color_number not in self.colors_options.keys():
            raise Exception("Invalid color")

        self.robot['color'] = self.colors_options[color_number]

    def get_part_attack(self, part: str) -> int:
        return self.robot["parts"][part].get_attack()


def config_robot():
    player = {}

    def set_player_name(player_dict: dict):
        name = input("Player name: ")
        player_dict["name"] = name

    set_player_name(player)
    robot_name = input("Your robot name: ")

    robot = Robot(name_player=player["name"], robot_name=robot_name)

    robot.show_color_options()
    color = int(input("Your robot color: "))
    robot.set_color(color)
    player["robot"] = robot

    return player["robot"]


def fight(robot_1: Robot, robot_2: Robot):
    while True:
        pass


def start():
    def initial(robot):
        robot.say_hi()
        robot.show_robot()

    print("Player 1 Configurations")
    robot_1 = config_robot()
    initial(robot_1)

    print("Player 2 Configurations")
    robot_2 = config_robot()
    initial(robot_2)


start()

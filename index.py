# this method select the component of robot to show if is available
from time import sleep

shield_art = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
def select_upper_body(robot_parts: dict):
    if robot_parts["head_status"] and robot_parts["weapon_status"]:
        return r"""
             1: {head_name}
             Is available: {head_status}
             Attack: {head_attack}                              
             Defense: {head_defense}
             Energy consumption: {head_energy_consump}
                      ^
                      |                  |2: {weapon_name}
                      |                  |Is available: {weapon_status}
             ____     |    ____          |Attack: {weapon_attack}
            |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
            |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consump}
            |oooo|/\_||_/\|oooo|"""

    elif not robot_parts["head_status"] and robot_parts["weapon_status"]:
        return r"""         
                                         |2: {weapon_name}
                                         |Is available: {weapon_status}
             ____          ____          |Attack: {weapon_attack}
            |oooo|        |oooo| ------> |Defense: {weapon_defense}
            |oooo|        |oooo|         |Energy consumption: {weapon_energy_consump}
            |oooo|        |oooo|"""

    elif not robot_parts["weapon_status"] and robot_parts["head_status"]:
        return r"""
             1: {head_name}
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
            `----' / __ \  `----'           |3: {left_arm_name}
           '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
           /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
          / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
         |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
         <_>      |=\__/=|      <_> ------> |
         <_>      |------|      <_>         |4: {right_arm_name}
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
               |_|| |/\| ||_|\_/ \          |4: {right_arm_name}
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
          / \_/|_|| |/\| ||_|               |3: {left_arm_name}
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
              | ||        || |          |5: {left_leg_name} 
             [==|]        [|==]         |Is available: {left_leg_status}
             [===]        [===]         |Attack: {left_leg_attack}
              >_<          >_<          |Defense: {left_leg_defense}
             || ||        || ||         |Energy consumption: {left_leg_energy_consump}
             || ||        || || ------> |
             || ||        || ||         |6: {right_leg_name}
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
                           >_<          |6: {right_leg_name}
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
              >_<                       |5: {left_leg_name}
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

    parts_options = {}

    def __init__(self, name_player: str, robot_name: str, default_robot_color: str = "blue"):
        for index, color in enumerate(self.colors):
            self.colors_options[index + 1] = color

        self.parts = {
            "head": Parts(name="Head", attack=10, defense=30, energy_consumption=30, selector="head"),
            "weapon": Parts(name="Missile Launcher", attack=50, defense=45, energy_consumption=100, selector="weapon"),
            "left_arm": Parts(name="Left Arm", attack=8, defense=38, energy_consumption=10, selector="left_arm"),
            "right_arm": Parts(name="Right Arm", attack=8, defense=38, energy_consumption=10, selector="right_arm"),
            "left_leg": Parts(name="Left Leg", attack=14, defense=40, energy_consumption=15, selector="left_leg"),
            "right_leg": Parts(name="Right Leg", attack=14, defense=40, energy_consumption=15, selector="right_leg")
        }

        for index, part in enumerate(self.parts.values()):
            self.parts_options[index + 1] = part.selector

        self.player = {
            "name": name_player
        }

        self.robot = {
            "name": robot_name,
            "parts": self.parts,
            "energy": 300,
            "color": default_robot_color
        }

    def say_hi(self):
        print(f"\nhello, i'm {self.robot['name']} and my boss is {self.player['name']}")

    def is_available_part(self, part: int) -> bool:
        return self.robot["parts"][self.parts_options[part]].is_available

    def is_all_parts_not_available(self):
        parts_available = []

        for part in self.robot["parts"].values():
            parts_available.append(part.is_available)

        return not (True in parts_available)

    def is_on(self) -> bool:
        return self.robot["energy"] >= 0

    def show_energy(self) -> None:
        energy = self.robot["energy"]

        color: str

        if energy >= 150:
            color = self.colors["green"]
        elif 50 <= energy < 150:
            color = self.colors["yellow"]
        else:
            color = self.colors["red"]
            print(self.colors["yellow"] + "A L E R T!".center(65))

        print(color + "=" * 65)
        print(f"{energy}% of energy".center(65))
        print("=" * 65 + self.stop_color)

    def show_parts_options(self, title="PARTS AVAILABLE"):
        message = f"\n{title}\n\n"

        for index, part in enumerate(self.parts.values()):
            if part.is_available:
                message += f"{index + 1} : {self.colors[self.robot['color']]} {part.name}{self.stop_color}\n"

        print(message)

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
               select_bottom_body(all_parts) +
               shield_art + self.stop_color).format(**all_parts))

    def decrease_energy(self, decrease: int):
        self.robot["energy"] -= decrease

    def decrease_part_defense(self, part: int, decrease: int):
        self.robot["parts"][self.parts_options[part]].decrease_defense(decrease)

    def show_color_options(self):
        message = f"\n\nAVAILABLE COLORS\n{'-' * 16}\n"

        colors_options_values = self.colors_options.values()
        for index, color in enumerate(colors_options_values):
            message += f"{index + 1} : {self.colors[color]} {color.capitalize()}{self.stop_color}\n"

        print(message)

    def set_color(self, color_number: int):
        if color_number not in self.colors_options.keys():
            raise Exception("Invalid color")

        self.robot['color'] = self.colors_options[color_number]

    def get_part(self, part: int):
        return self.robot["parts"][self.parts_options[part]]

    def get_part_attack(self, part: int) -> int:
        return self.robot["parts"][self.parts_options[part]].get_attack()


def config_robot() -> Robot:
    name = input("Player name: ")
    robot_name = input("Your robot name: ")

    robot = Robot(name_player=name, robot_name=robot_name)

    robot.show_color_options()
    color = int(input("Your robot color: "))
    robot.set_color(color)

    return robot


def start():
    def initial(robot):
        robot.say_hi()
        robot.show_robot()

    def check_winner(robot_1: Robot, robot_2: Robot):
        robot_1_win = f"\n\nNice {robot_1.player['name']}, your robot {robot_1.robot['name']} won this game"
        robot_2_win = f"\n\nNice {robot_2.player['name']}, your robot {robot_2.robot['name']} won this game"
        if not robot_1.is_on():
            print(robot_2_win)
            return True
        elif not robot_2.is_on():
            print(robot_1_win)
            return True
        elif robot_1.is_all_parts_not_available():
            print(robot_2_win)
        elif robot_2.is_all_parts_not_available():
            print(robot_1_win)
            return True
        return False

    print("Player 1 Configurations")
    robot_1 = config_robot()
    initial(robot_1)

    print("Player 2 Configurations")
    robot_2 = config_robot()
    initial(robot_2)

    sleep(1)
    while True:
        fight(robot=robot_1, enemy=robot_2, player_number=1)
        if check_winner(robot_1, robot_2):
            break
        fight(robot=robot_2, enemy=robot_1, player_number=2)
        if check_winner(robot_1, robot_2):
            break


def fight(robot: Robot, enemy: Robot, player_number: int):
    print(f"\n\n== Player {player_number} fight ==\n\n")
    robot.show_robot()
    robot.show_energy()
    robot.show_parts_options()

    while True:
        part_to_use = int(input("Select one part to fight: (ex: head) "))
        if not robot.is_available_part(part=part_to_use):
            print("You can't use that part, it is not available!")
        else:
            break

    print("\nChoose enemy part to attack")
    enemy.show_parts_options()
    while True:
        enemy_part_to_attack = int(input("Select enemy part to attack: "))
        if not enemy.is_available_part(part=enemy_part_to_attack):
            print("You can't attack this part, it is not available!")
        else:
            break

    attack = robot.get_part_attack(part_to_use)
    robot.decrease_energy(robot.get_part(part_to_use).energy_consumption)
    enemy.decrease_part_defense(decrease=attack, part=enemy_part_to_attack)


start()

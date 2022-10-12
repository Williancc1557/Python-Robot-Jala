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
        print(self.colors[color] + rf"""
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
            |oooo|/\_||_/\|oooo|          
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
        \__/  _|||        |||_  \__/        
              | ||        || |          |4: {robot_parts["left_leg"]["name"]} 
             [==|]        [|==]         |Is available: {robot_parts["left_leg"]["is_available"]}
             [===]        [===]         |Attack: {robot_parts["left_leg"]["attack"]}
              >_<          >_<          |Defense: {robot_parts["left_leg"]["defense"]}
             || ||        || ||         |Energy consumption: {robot_parts["left_leg"]["energy_consumption"]}
             || ||        || || ------> |
             || ||        || ||         |5: {robot_parts["left_leg"]["name"]}
           __|\_/|__    __|\_/|__       |Is available: {robot_parts["left_leg"]["is_available"]}
          /___n_n___\  /___n_n___\      |Attack: {robot_parts["left_leg"]["attack"]}
                                        |Defense: {robot_parts["left_leg"]["defense"]}
                                        |Energy consumption: {robot_parts["left_leg"]["energy_consumption"]}

        """)


RobotsWar("Willian", "Junin")

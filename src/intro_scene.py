import math
from src.scene import Scene
from src.minion_scene import MinionScene

import time


class IntroScene(Scene):
    def __init__(self, player: dict) -> None:
        super().__init__(player)

    def display(self):
        print("Welcome player, you have been summoned to defeat C'tri the Lord of fire")
        time.sleep(1)

        return

    def interact(self) -> str:

        self.player["name"] = input(">>> What shall thou be called henceforth? ")
        print(f"We are happy to have you with us {self.player['name']}")

    def get_next_scene(self):
        return MinionScene(self.player)


class DeathScene(Scene):
    def __init__(self, player: dict, cause: str, epitath: str) -> None:
        super().__init__(player)
        self.cause = cause
        player_name_fomatted = player.get("name", "John doe")[0:30]
        padding_l = math.floor((30 - player_name_fomatted) / 2)
        padding_r = math.ceil((30 - player.get()))
        player_name_fomatted = f"{padding_l}{player_name_fomatted}{padding_r}"
        print(
            f"""
                  _____  _____
                 <     `/     |
                 >           (
                 |   _     _  |
                 |  |_) | |_) |
                 |  | \ | |   |
                 |            |
  ______.______%_|            |__________  _____
_/   {player_name_fomatted}              \|     |
|     {epitath}                                 <
|_____.-._________             ____/|___________|
                 |            |
                 | + {death_date} |
                 |            |
                 |            |
                 |   _        <
                 |__/         |
                  / `--.      |
                %|            |%
            |/.%%|          -< @%%%
            `\%`@|     v      |@@%@%%    - mfj
          .%%%@@@|%    |    % @@@%%@%%%%
     _.%%%%%%@@@@@@%%_/%\_%@@%%@@@@@@@%%%%%%
        
        {cause_of_death} """
        )

    def _center_and_trim(text:str) -> str:
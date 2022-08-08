import math
from src.scene import Scene
import src.minion_scene as minion_scenes
from datetime import datetime

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
        return minion_scenes.MinionScene(self.player)


class DeathScene(Scene):
    def __init__(self, player: dict, cause: str, epitath: str) -> None:
        super().__init__(player)
        self.cause = cause
        self.epitath = epitath

    def display(self) -> None:
        player_name = _center_and_trim(self.player.get("name", "John Doe"), 33)
        epitath = _center_and_trim(self.epitath, 32)
        cause_of_death = _center_and_trim(self.cause)
        death_date = datetime.strftime(datetime.now(), "%y-%b-%d")
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
_/   {player_name}   \|     |
|     {epitath}         <
|_____.-._________             ____/|___________|
                 |            |
                 | +{death_date} |
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

    def interact(self) -> None:
        time.sleep(1)

        print("Press enter to continue")
        input(">>> ")
        return


def _center_and_trim(text: str, max_len: int = 30) -> str:
    out_str = text if text != "" else "John doe"
    out_str = out_str[0:max_len]
    padding_l = math.floor((max_len - len(text)) / 2)
    padding_l = " " * padding_l
    padding_r = math.ceil((max_len - len(text)) / 2)
    padding_r = " " * padding_r
    out_str = f"{padding_l}{out_str}{padding_r}"
    return out_str

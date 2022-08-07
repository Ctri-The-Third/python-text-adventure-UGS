import math
from src.scene import Scene
from src.minion_scene import MinionScene
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
        return MinionScene(self.player)


class DeathScene(Scene):
    def __init__(self, player: dict, cause: str, epitath: str) -> None:
        super().__init__(player)
        self.cause = cause
        self.epitath = epitath

    def display(self) -> None:
        player_name = _center_and_trim(self.player.get("name", "John Doe"))
        epitath = _center_and_trim(self.epitath, 28)
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
|     {epitath}                                 <
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


def _center_and_trim(text: str, max_len: int = 30) -> str:
    out_str = text("name", "John doe")[0:max_len]
    padding_l = math.floor((max_len - text) / 2)
    padding_r = math.ceil((max_len - text))
    out_str = f"{padding_l}{out_str}{padding_r}"
    return out_str

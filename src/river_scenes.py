from src.intro_scene import Scene
import src.boss_scenes as boss_scenes


class river_scene(Scene):
    def __init__(self, player: dict) -> None:
        self.player = player
        self.choice = ""

    def display(self) -> None:
        print("You find yourself in front of a very pretty river. What will you do?")

    def interact(self) -> None:
        print("A. Nothing \nB. Fill bucket (CONDITIONAL)\n X. save & exit game")

    def get_next_scene(self):

        return boss_scenes.boss_battle_intro(self.player)

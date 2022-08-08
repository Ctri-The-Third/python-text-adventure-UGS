import random
from src.scene import Scene
import src.intro_scene as intro_scenes
import src.river_scenes as river_scenes
import time


class MinionScene(Scene):
    def __init__(self, player: dict) -> None:
        super().__init__(player)
        self.valid_answers = ["A", "B", "C", "X"]

    def display(self):
        time.sleep(1)
        print("***INTERRUPTION***")
        time.sleep(2)
        print(
            "A minion has appeared, but rest assured, you are not without deadly options!!! You look around the room and see a bucket and a stick\n"
        )
        print(
            """
    
                    ..::.  .::..                     
                .::^^~!!:^!!~^^::.                  
                ::::::::::::::^^^^^:                 
                .:..:::::::::::^^^^^^.                
            ...:^!!!~~~~^^~~!!!!~~^.               
            .::~77~^^^!7!~7~^:^~77!!^.              
            .JY~?7. :??^77?~~?7. :?7JP7              
            ~7^77: ^?7^!!7!~?7..^7!!?^              
            .:^!7~~~~!~7!!!~~~!7~^~^               
            ..:::^^~~~!777!~~~~~~~~~^.              
            .:::::^^^^^^^^^~~~~~~~~^               
            ::.::::::::^^^^^^^^^^^^^~:              
            !!~::::::::::::::^^^^~!?5?              
            :~77?7!!~!!!!!!!77?JY5P5?^              
            .:::!55Y?JJYYYY5555PGGP7~~~:             
            .:^^::????JJJ5PPP55555PY^^!!^             
            .:7~:^7????JYGGGB55555PJ~!J?^.            
            :?77?????JYY5PP5555555555PJ^             
            ^!JYJJ?JJJYYYY5555555555PPGY7:            
            7B#BYYY55555555PPPPPPP555Y##B^            
            JBB&&Y.:~5GBBBJ5#BB#G7!!B@#BB?~~~^^^::.   
            :^757  ..7#&&B7?B&&#?777?PBYJ?777777!~:.  
            .::::^!5##BY775###Y!!!!~~~~^^:::...     
                    :::.   ..::..                  
    """
        )

    def interact(self) -> None:
        time.sleep(1)
        print(
            """  A. Grab the bucket and throw it at the minion
  B. grab a stick and poke the miRnion
  C. Run
  
  X. Exit adventure"""
        )
        self.choice = ""
        while self.choice not in self.valid_answers:
            self.choice = input(">>> ").upper()

    def get_next_scene(self):

        if self.choice == self.valid_answers[0]:  # A
            return BucketScene(self.player)
        elif self.choice == self.valid_answers[1]:
            return StickScene(self.player)
        elif self.choice == self.valid_answers[2]:
            return intro_scenes.DeathScene(
                self.player, "The 4 legged minion easily chases you down!", ""
            )


class BucketScene(Scene):
    def __init__(self, player: dict) -> None:
        super().__init__(player)


class StickScene(Scene):
    def __init__(self, player: dict) -> None:
        super().__init__(player)
        self.victory = False
        self.outcome = ""

    def display(self) -> None:
        print(
            "\nYou pick up the stick and swing at the minion, doing incredible battle"
        )
        time.sleep(0.25)

        print("working...")
        time.sleep(1)

        if random.randint(0, 20) == 1:
            print("Critical fail! You throw the stick. Maybe it likes to play fetch?")
            self.outcome = "FAIL"
        elif random.randint(0, 20) > 5:
            print(
                "Victory! You bop the enemy over the head and it pops like a balloon!"
            )
            self.outcome = "VICTORY"
        else:
            self.outcome = "fail"
            print(
                """The creature snatches your stick in its teeth and begins tearing at it! 
you're able to escape whilst it's distracted, but you lose your stick."""
            )

    def interact(self) -> None:
        return

    def get_next_scene(self):
        if self.outcome == "VICTORY":
            return river_scenes.river_scene(self.player)
        elif self.outcome == "FAIL":
            return intro_scenes.DeathScene(
                self.player,
                "You dropped your weapon in a fight! It didn't end well.",
                "Ole slippy fingers",
            )

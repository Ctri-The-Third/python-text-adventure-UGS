import time  # Imports a module to add a pause
from src.scene import Scene

# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

playerName = ""

required = "\nUse only A, B, or C\n"  # Cutting down on duplication

# The story is broken into sections, starting with "intro"

intro_scene = Scene()
intro_scene.display()
intro_scene.interact()
next_scene = intro_scene.get_next_scene()

while True:
    next_scene: Scene
    next_scene.display()
    next_scene.interact()
    next_scene = next_scene.get_next_scene()

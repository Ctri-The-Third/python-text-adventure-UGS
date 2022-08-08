import time
from src.scene import Scene
import src.minion_scene as minion_scenes
from src.intro_scene import DeathScene, IntroScene

# The story is broken into sections, starting with "intro"
player = {}
player["name"] = "Harold rocksbeater"
intro_scene = minion_scenes.StickScene(player)
intro_scene.display()
intro_scene.interact()
next_scene = intro_scene.get_next_scene()

while True:
    next_scene: Scene
    next_scene.display()
    next_scene.interact()
    next_scene = next_scene.get_next_scene()

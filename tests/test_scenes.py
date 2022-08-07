import sys

sys.path.append("")

from src.scene import Scene
import src.intro_scene as intro_scenes


def test_intro():
    player = {"name": "tester testerson"}
    scene: Scene = intro_scenes.IntroScene(player)
    scene.display()
    _is_valid_scene(scene)

    next_scene = scene.get_next_scene()
    assert issubclass(next_scene.__class__, Scene)


def test_death_init():
    player = {"name": "tester testerson"}
    scene: Scene = intro_scenes.DeathScene(
        player, "eaten by a grue", "died before his time"
    )
    _is_valid_scene(scene)
    scene.display()

    next_scene = scene.get_next_scene()
    assert issubclass(next_scene.__class__, Scene)


def _is_valid_scene(scene):
    assert issubclass(scene.__class__, Scene)

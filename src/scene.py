from abc import abstractmethod


class Scene:
    def __init__(self, player: dict) -> None:
        self.player = player

    @abstractmethod
    def display(self) -> None:
        "displays the intro scene"
        raise NotImplementedError

    @abstractmethod
    def interact(self) -> None:
        "displays a thing and repeats input until a valid option is selected, returns the valid option"
        raise NotImplementedError

    @abstractmethod
    def get_next_scene(self):
        "returns the next scene the user should experience"
        raise NotImplementedError

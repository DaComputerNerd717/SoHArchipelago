import typing

from BaseClasses import Region, MultiWorld


class SoHRegion(Region):
    game: str = "Ocarina of Time (SoH)"

    def __init__(self, name: str, player: int, game: MultiWorld):
        super(SoHRegion, self).__init__(name, player, game)
        self.scene: str
        self.time_passes: bool = False
        self.event_access: typing.List[str] = []
        self.locations: typing.List[str] = []
        self.exits: typing.List[str] = []

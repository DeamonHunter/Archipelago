from test.bases import WorldTestBase
from .. import Everhood2World
from typing import cast

class Everhood2TestBase(WorldTestBase):
    game = "Everhood 2"

    def get_world(self) -> Everhood2World:
        return cast(Everhood2World, self.multiworld.worlds[1])


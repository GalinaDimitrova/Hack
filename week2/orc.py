from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        # self.name = name
        # self.health = health
        super().__init__(name, health)
        self._set_selfberserk_factor(berserk_factor)
        self._MAX_HEALTH = health

    # it is used only in the class

    def _set_selfberserk_factor(self, berserk_factor):
        if berserk_factor >= 1 and berserk_factor <= 2:
            self.berserk_factor = berserk_factor
        # else:
        #     raise ValueError
        elif berserk_factor < 1:
            self.berserk_factor = 1.0
        else:
            self.berserk_factor = 2.0

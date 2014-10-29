import random


class Weapon:

    def __init__(self, type, damage, critical_strike_percent):
        self.type = type
        self.damage = damage
        #self.critical_strike_percent = critical_strike_percent
        self._set_critical_strike_persent(critical_strike_percent)

    def _set_critical_strike_persent(self, critical_strike_percent):
        if critical_strike_percent > 0 and critical_strike_percent < 1:
            self.critical_strike_percent = critical_strike_percent
        else:
            raise ValueError

    def critical_hit(self):
        if random.random() > self.critical_strike_percent:
            return False
        return True

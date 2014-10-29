import random
from hero import Hero
from orc import Orc


class Fight(Hero, Orc):

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def simulate_battle(self):
        attacker = self.attack_first()
        if attacker == self.hero:
            attacked = self.orc
        else:
            attacked = self.hero

        while self.orc.is_alive() and self.hero.is_alive():
            damage = attacker.attack()
            attacked.take_damage(damage)
            # razmenqme atakuva6tiq
            print("{} is the first fighter and has health: {}".format(attacker.name, attacker.get_health()))
            attacked, attacker = attacker, attacked

    def attack_first(self):
        first = random.randint(1, 100)
        if first <= 50:
            return self.hero
        else:
            return self.orc

import unittest
import fight
from hero import Hero
from orc import Orc
from weapon import Weapon


class FightTest(unittest.TestCase):

    def setUp(self):
        self.hero_one = Hero("Bron", 100, "DragonSlayer")
        self.orc_one = Orc("Orcy", 150, 1.5)
        self.fight_one = fight.Fight(self.hero_one, self.orc_one)
        self.axe = Weapon("Axe", 20, 0.2)
        self.sword = Weapon("Sword", 12, 0.7)
        self.hero_one.weapon = self.sword
        self.orc_one.weapon = self.axe

    def test_init(self):
        self.assertEqual(self.fight_one.hero, self.hero_one)
        self.assertEqual(self.fight_one.orc, self.orc_one)

    def test_fight(self):
        self.fight_one.simulate_battle()
        # if one of them died
        self.assertFalse(self.orc_one.is_alive() and self.hero_one.is_alive())

    def test_fight_no_weapon(self):
        self.orc_one.weapon = None
        self.fight_one.simulate_battle()
        # orc has no weapon => orc dies
        self.assertFalse(self.orc_one.is_alive())

    def test_fight_equal(self):
        hero_one = Hero("Bron", 100, "DragonSlayer")
        orc_one = Orc("Orcy", 150, 1.5)
        hero_one.weapon = Weapon("Axe", 20, 0.5)
        orc_one.weapon = Weapon("Axe", 20, 0.5)
        self.fight_one.simulate_battle()
        # both has the same weapon, but the orc has berserc_factor,\
        # he should be alive at the end
        self.assertTrue(self.orc_one.is_alive())


if __name__ == '__main__':
    unittest.main()

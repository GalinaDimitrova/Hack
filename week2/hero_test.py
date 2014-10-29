import unittest
import hero


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.bron_hero = hero.Hero("Bron", 100, "DragonSlayer")

    def test_hero_init(self):
        # self.assertEqual(self.bron_hero.name, "Bron")
        # self.assertEqual(self.bron_hero.health, 100)
        self.assertEqual(self.bron_hero.nickname, "DragonSlayer")

    def test_known_as(self):
        self.assertEqual(
            self.bron_hero.known_as(), "Bron the DragonSlayer")

    # def test_get_health(self):
    #     self.assertEqual(self.bron_hero.get_health(), 100)

    # def test_is_alive(self):
    #     self.assertTrue(self.bron_hero.is_alive())
    #     # we don't need self infront of hero becaouse this change is \
    #     # is supposed to be used only here
    #     self.bron_hero.health = 0
    #     self.assertFalse(self.bron_hero.is_alive())

    # def test_take_damage_int(self):
    #     self.bron_hero.take_damage(10)
    #     self.assertEqual(self.bron_hero.get_health(), 90)

    # def test_take_damage_float(self):
    #     self.bron_hero.take_damage(1.50)
    #     self.assertEqual(self.bron_hero.get_health(), 98.5)

    # def test_take_damage_more_than_it_can(self):
    #     self.bron_hero.take_damage(150)
    #     self.assertEqual(self.bron_hero.get_health(), 0)

    # def test_take_healing(self):
    #     self.bron_hero.health = 40
    #     result_healing = self.bron_hero.take_healing(20)
    #     self.assertEqual(self.bron_hero.health, 60)
    #     self.assertTrue(result_healing)

    # def test_take_healing_when_it_cannot(self):
    #     self.bron_hero.health = 0
    #     result_healing = self.bron_hero.take_healing(20)
    #     self.assertEqual(self.bron_hero.health, 0)
    #     self.assertFalse(result_healing)

    # def test_take_healing_more_than_it_can(self):
    #     self.bron_hero.health = 90
    #     result_healing = self.bron_hero.take_healing(20)
    #     self.assertEqual(self.bron_hero.health, self.bron_hero._MAX_HEALTH)
    #     self.assertTrue(result_healing)


if __name__ == '__main__':
    unittest.main()

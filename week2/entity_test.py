import unittest
import entity

from weapon import Weapon


class EntityTest(unittest.TestCase):

    def setUp(self):
        self.bron_entity = entity.Entity("Bron", 100)

    def test_hero_init(self):
        self.assertEqual(self.bron_entity.name, "Bron")
        self.assertEqual(self.bron_entity.health, 100)

    def test_get_health(self):
        self.assertEqual(self.bron_entity.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.bron_entity.is_alive())
        # we don't need self infront of hero becaouse this change is \
        # is supposed to be used only here
        self.bron_entity.health = 0
        self.assertFalse(self.bron_entity.is_alive())

    def test_take_damage_int(self):
        self.bron_entity.take_damage(10)
        self.assertEqual(self.bron_entity.get_health(), 90)

    def test_take_damage_float(self):
        self.bron_entity.take_damage(1.50)
        self.assertEqual(self.bron_entity.get_health(), 98.5)

    def test_take_damage_more_than_it_can(self):
        self.bron_entity.take_damage(150)
        self.assertEqual(self.bron_entity.get_health(), 0)

    def test_take_healing(self):
        self.bron_entity.health = 40
        result_healing = self.bron_entity.take_healing(20)
        self.assertEqual(self.bron_entity.health, 60)
        self.assertTrue(result_healing)

    def test_take_healing_when_it_cannot(self):
        self.bron_entity.health = 0
        result_healing = self.bron_entity.take_healing(20)
        self.assertEqual(self.bron_entity.health, 0)
        self.assertFalse(result_healing)

    def test_has_weapon(self):
        self.assertFalse(self.bron_entity.has_weapon())
        self.bron_entity.weapon = "Axe"
        self.assertTrue(self.bron_entity.has_weapon())

    def test_equip_weapon(self):
        my_axe = Weapon("Axe", 20, 0.5)
        self.bron_entity.equip_weapon(my_axe)
        self.assertEqual(self.bron_entity.weapon, my_axe)

    def test_equip_new_weapon(self):
        my_axe = Weapon("Axe", 20, 0.5)
        self.bron_entity.equip_weapon(my_axe)
        sword = Weapon("Sword", 30, 0.5)
        self.bron_entity.equip_weapon(sword)
        self.assertEqual(self.bron_entity.weapon, sword)

    def test_attack_no_weapon(self):
        self.bron_entity.weapon = None
        self.assertEqual(self.bron_entity.attack(), 0)

    def test_attack_with_weapon(self):
        my_axe = Weapon("Axe", 20, 0.5)
        self.bron_entity.equip_weapon(my_axe)
        damage_made = self.bron_entity.attack()
        self.assertGreaterEqual(damage_made, 20)
        #self.assertIn(damage_made,[20, 40])




if __name__ == '__main__':
    unittest.main()

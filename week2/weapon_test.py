import unittest
import weapon


class WeaponTese(unittest.TestCase):

    def setUp(self):
        self.weapon = weapon.Weapon("Mighty Axe", 25, 0.2)

    def test_weapon_init(self):
        self.assertEqual(self.weapon.type, "Mighty Axe")
        self.assertEqual(self.weapon.damage, 25)

    def test_critical_strike_percent_in_range(self):
        self.weapon._set_critical_strike_persent(0.2)
        self.assertEqual(self.weapon.critical_strike_percent, 0.2)

    def test_critical_strike_percent_not_in_range(self):
        with self.assertRaises(ValueError):
            weapon.Weapon("Mighty Axe", 25, 5)

    def test_critical_hit(self):
        axe = weapon.Weapon("Axe", 10, 0.5)
        results = []
        for i in range(1000):
            results.append(axe.critical_hit())
        self.assertTrue(True in results)
        self.assertTrue(False in results)


if __name__ == '__main__':
    unittest.main()

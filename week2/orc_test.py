import unittest
import orc


class OrcTest(unittest.TestCase):

    def setUp(self):
        self.orc = orc.Orc("Orcy", 150, 1.5)

    def test_orc_init(self):
        self.assertEqual(self.orc.name, "Orcy")
        self.assertEqual(self.orc.health, self.orc._MAX_HEALTH)
    # tests if we raised value error

    # def test_orc_berserk_factor(self):
    #     self.assertRaises(ValueError, hero.Orc("Ivo", 20))

    def test_init_berserk_factor_in_range(self):
        #self.orc.berserk_factor = 2
        self.orc._set_selfberserk_factor(5)
        self.assertEqual(self.orc.berserk_factor, 2.0)

    def test_init_berserk_factor_test_not_in_range(self):
        self.orc._set_selfberserk_factor(5)
        self.assertEqual(self.orc.berserk_factor, 2.0)
        self.orc._set_selfberserk_factor(0)
        self.assertEqual(self.orc.berserk_factor, 1.0)

    #def test_attack(self):


if __name__ == '__main__':
    unittest.main()

import unittest
from song import Song


class SongTest(unittest.TestCase):

    def setUp(self):
        self.song = Song(
            "Desert rose", "Sting", "Brand New Day", 0.0, "4:45", 8)

    def test_init(self):
        self.assertEqual(self.song.title, "Desert rose")
        self.assertEqual(self.song.artist, "Sting")
        self.assertEqual(self.song.album, "Brand New Day")
        self.assertEqual(self.song.rating, 0.0)
        self.assertEqual(self.song.length, "4:45")
        self.assertEqual(self.song.bitrate, 8)

    def test_rate(self):
        self.song.rate(4)
        self.assertEqual(self.song.rating, 4.0)

    def test_rong_rate(self):
        self.assertRaises(ValueError, self.song.rate, 6)


if __name__ == '__main__':
    unittest.main()

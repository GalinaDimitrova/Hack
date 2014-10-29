import unittest
from song import Song
from playlist import Playlist


class PlaylistTest(unittest.TestCase):
    def setUp(self):
        self.my_playlist = Playlist("myList")
        self.song = Song(
            "Desert rose", "Sting", "Brand New Day", 4.0, "4:45", 8)
        self.song1 = Song(
            "Hells Bells", "ACDC", "Brand New Day", 5.0, "05:09", 8)
        self.song2 = Song(
            "Baby, Please Don't Go", "ACDC", "Brand New Day", 1.0, "03:51", 8)
        self.song3 = Song(
            "I Want It That Way", "Backstreet Boys", "Brand New Day", 3.0, "05:00", 8)


    # def tearDown(self):
    #     #d.cleanup()
    #     TempDirectory.cleanup_all()

    def test_init(self):
        self.assertEqual(self.my_playlist.playlist_name, "myList")

    def test_add_song(self):
        self.my_playlist.add_song(self.song)
        self.assertIn(self.song, self.my_playlist.songs)
        self.my_playlist.add_song(self.song1)
        self.assertIn(self.song1, self.my_playlist.songs)

    def test_add_song_wrong_format(self):
        self.assertRaises(ValueError, self.my_playlist.add_song, (
            "Desert rose", "Sting", "Brand New Day"))


    def test_remove_song(self):
        self.my_playlist.add_song(self.song)
        self.my_playlist.add_song(self.song1)
        self.my_playlist.add_song(self.song)
        self.my_playlist.remove_song(self.song.title)
        self.assertNotIn(self.song, self.my_playlist.songs)

    def test_total_length(self):
        self.my_playlist.add_song(self.song)
        self.my_playlist.add_song(self.song)
        self.my_playlist.add_song(self.song3)
        self.assertEqual(self.my_playlist.total_length(), "14:30")

    def test_remove_disrated(self):
        self.my_playlist.add_song(self.song)
        self.my_playlist.add_song(self.song1)
        self.my_playlist.add_song(self.song2)
        self.my_playlist.add_song(self.song3)
        self.my_playlist.remove_disrated(4)
        self.assertNotIn(self.my_playlist.songs, [self.song2, self.song3])

    def test_remove_disrated_not_in_range(self):
        self.assertRaises(ValueError, self.my_playlist.remove_disrated, 6)

    def test_show_artists(self):
        self.my_playlist.add_song(self.song)
        self.my_playlist.add_song(self.song1)
        self.my_playlist.add_song(self.song3)
        self.assertEqual(self.my_playlist.show_artists(), [
            "Sting", "ACDC", "Backstreet Boys"])

    def test_show_artists_without_duplicate(self):
        self.my_playlist.add_song(self.song)
        self.my_playlist.add_song(self.song)
        self.my_playlist.add_song(self.song)
        self.assertEqual(self.my_playlist.show_artists(), ["Sting"])

    def test_str(self):
        self.my_playlist.add_song(self.song)
        self.my_playlist.add_song(self.song1)
        self.assertEquals(self.my_playlist.str(),[
            "Sting Desert rose - 4:45", "ACDC Hells Bells - 05:09"])


    def test_save(self):
        self.my_playlist.add_song(self.song)
        self.my_playlist.add_song(self.song)
        self.my_playlist.save("list1.txt")
        pass
    
    def test_load(self):
        self.my_playlist.load("list_load.txt")




if __name__ == '__main__':
    unittest.main()
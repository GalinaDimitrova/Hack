from song import Song
import json


class Playlist:
    LOW_BIRATE = 64

    def __init__(self, playlist_name=None):
        self.songs = []
        self.playlist_name = playlist_name

    def add_song(self, song):
        if type(song) is Song:
            self.songs.append(song)
        else:
            raise ValueError(
                'Wrong type of arguments! Given {}'.format(type(song)))

    def remove_song(self, song_name):
        for i in range(len(self.songs) - 1, -1, -1):
            if self.songs[i].title == song_name:
                del self.songs[i]

    def total_length(self):
        song_length = []
        minutes = 0
        seconds = 0
        for item in self.songs:
            song_length = item.length.split(":")
            seconds += int(song_length[1])
            minutes += int(song_length[0])
        if seconds >= 60:
            minutes += seconds // 60
            seconds = seconds % 60
        return ":".join([str(minutes), str(seconds)])

    def remove_disrated(self, rate):
        if rate < 0 or rate > 5:
            raise ValueError("Not in range(0:5)!")
        for item in self.songs:
            if item.rating < rate:
                self.remove_song(item.title)

    def remove_bad_quality(self):
        pass

    def show_artists(self):
        artists = []
        for item in self.songs:
            if item.artist not in artists:
                artists.append(item.artist)
        return artists

    def str(self):
        str_song = []
        for item in self.songs:
            str_song.append(
                "{} {} - {}".format(item.artist, item.title, item.length))
        return str_song

    def save(self, file_name):
        songs_dict = {}
        songs_dict["name"] = self.playlist_name
        songs_dict["songs"] = []

        for i in range(len(self.songs)):
            songs_dict["songs"].append(self.songs[i].__dict__)
        with open(file_name, 'w') as outfile:
            json.dump(songs_dict, outfile)

    def load(self, file_name):
        infile = open(file_name)
        data = json.load(infile)

        self.playlist_name = data["name"]
        for i in range(len(data["songs"])):
            self.songs.append(Song(
                data["songs"][i]["title"],
                data["songs"][i]["artist"],
                data["songs"][i]["album"],
                data["songs"][i]["rating"],
                data["songs"][i]["length"],
                data["songs"][i]["bitrate"]))
        # print(self.songs)

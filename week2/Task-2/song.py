class Song:
    MAX_RATE = 5
    MIN_RATE = 0

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate
        self.count_raters = 0

    def rate(self, rate):
        if rate >= MIN_RATE and rate <= MAX_RATE:
            self.count_raters += 1
            self.rating = (self.rating + rate) / self.count_raters
        else:
            raise ValueError("Not in range(0:5)!")

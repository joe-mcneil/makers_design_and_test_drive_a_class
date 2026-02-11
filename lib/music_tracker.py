
class MusicTracker:
    def __init__(self):
        self.tracks = []

    def add_track(self, artist, track):
        self.tracks.append({"artist": artist, "track": track})

    def list_tracks(self):
        return self.tracks
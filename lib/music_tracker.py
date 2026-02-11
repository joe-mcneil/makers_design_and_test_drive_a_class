
class MusicTracker:
    def __init__(self):
        self.tracks = []

    def add_track(self, artist, track):
        if type(artist) == str and type(track) == str:
            self.tracks.append({"artist": artist, "track": track})
        else:
            raise Exception("Invalid track.")

    def list_tracks(self):
        if len(self.tracks) > 0:
            return self.tracks
        else:
            raise Exception("No tracks yet.")
from lib.music_tracker import *
import pytest

def test_add_single_track_to_tracker():
    tracker = MusicTracker()
    tracker.add_track("Beatles", "Yesterday")
    actual = tracker.list_tracks()
    expected = [{"artist": "Beatles", "track": "Yesterday"}]

    assert actual == expected
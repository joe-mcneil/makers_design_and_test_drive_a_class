from lib.music_tracker import *
import pytest

def test_add_single_track_to_tracker():
    tracker = MusicTracker()
    tracker.add_track("Beatles", "Yesterday")
    actual = tracker.list_tracks()
    expected = [{"artist": "Beatles", "track": "Yesterday"}]

    assert actual == expected

def test_add_multiple_track_to_tracker():
    tracker = MusicTracker()
    tracker.add_track("Beatles", "Yesterday")
    tracker.add_track("Radiohead", "Creep")
    actual = tracker.list_tracks()
    expected = [{"artist": "Beatles", "track": "Yesterday"},
                {"artist": "Radiohead", "track": "Creep"}]

    assert actual == expected

def test_adding_no_track_to_tracker():
    tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        tracker.add_track()
    actual = str(e.value)
    expected = "Invalid track."

    assert actual == expected

def test_adding_invalid_type_to_tracker():
    tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        tracker.add_track(12)
    actual = str(e.value)
    expected = "Invalid track."

    assert actual == expected

def test_no_tracks_and_empty_list():
    tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        tracker.list_tracks()
    actual = str(e.value)
    expected = "No tracks yet."

    assert actual == expected
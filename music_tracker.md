# Music Tracker Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker:
    # User-facing properties:
    #   add_track, list_tracks

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   Creates an empty list to store tracks
        pass  # No code here yet

    def add_track(self, artist, track):
        # Parameters:
        #   artist: string representing track artist
        #   track: string representing track name
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves {artist: "artist", track: "track"} to the self object
        pass  # No code here yet

    def list_track(self):
        # Returns:
        #   Our list of dictionaries of artists and tracks
        pass  # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Adding a single track
returns artist and track
"""
tracker = MusicTracker()
tracker.add_track("Beatles", "Yesterday")
tracker.list_tracks() # => [{"artist": "Beatles", "track": "Yesterday"}]

"""
Adding multiple tracks
returns artists and tracks as a list
"""
    tracker = MusicTracker()
    tracker.add_track("Beatles", "Yesterday")
    tracker.add_track("Radiohead", "Creep")
    tracker.list_tracks() # => [{"artist": "Beatles", "track": "Yesterday"}, {"artist": "Radiohead", "track": "Creep"}]

"""
Adding no tracks/adding none
rasises an exception
"""
tracker = MusicTracker()
tracker.add_track() # raises an error with the message "Invalid track."

"""
Adding invalid type as track
rasises an exception
"""
tracker = MusicTracker()
tracker.add_track(12, 15) # raises an error with the message "Invalid track."

"""
Adding no tracks and asking to list
rasises an exception
"""
tracker = MusicTracker()
tracker.list_tracks() # raises an error with the message "No tracks yet"


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

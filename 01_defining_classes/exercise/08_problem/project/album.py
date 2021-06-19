class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = []
        self.published = False
        for i in args:
            self.songs.append(i)

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."
        else:
            for song in self.songs:
                if song_name == song.name:
                    self.songs.remove(song)
                    return f"Removed song {song_name} from album {self.name}."
            else:
                return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"
        return result

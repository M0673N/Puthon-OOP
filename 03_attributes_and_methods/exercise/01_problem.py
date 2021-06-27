class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)

    def add_photo(self, label):
        for page in range(1, len(self.photos) + 1):
            if len(self.photos[page - 1]) < 4:
                self.photos[page - 1].append(label)
                slot = self.photos[page - 1].index(label) + 1
                return f"{label} photo added successfully on page {page} slot {slot}"
        else:
            return "No more free slots"

    def display(self):
        result = "-" * 11 + "\n"
        for page in self.photos:
            if len(page) == 0:
                result += "\n" + "-" * 11 + "\n"
            else:
                for photo in page:
                    result += "[] "
                result = result.rstrip()
                result += "\n"
                result += "-" * 11 + "\n"
        return result


# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())

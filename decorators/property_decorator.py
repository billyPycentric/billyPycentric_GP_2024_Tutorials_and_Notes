# Used for guaging access -> making data/var private
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property    # Getter
    def radius(self):
        return self._radius
    @radius.setter # Setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Invalid radius Value")

    @radius.deleter
    def radius(self):
        print("Deleted")
        del self.radius
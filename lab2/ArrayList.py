class ArrayList:
    def __init__(self):
        self.items = []

    def length(self):
        return len(self.items)

    def append(self, ch):
        self.validate_char(ch)
        self.items.append(ch)

    def delete(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of bounds")
        return self.items.pop(index)

    def insert(self, ch, index):
        self.validate_char(ch)
        if index < 0 or index > len(self.items):
            raise IndexError("Index out of bounds")
        self.items.insert(index, ch)

    def deleteAll(self, ch):
        self.validate_char(ch)
        self.items = [x for x in self.items if x != ch]

    def get(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of bounds")
        return self.items[index]

    def clone(self):
        copy = ArrayList()
        copy.items = self.items.copy()
        return copy

    def reverse(self):
        self.items.reverse()

    def findFirst(self, ch):
        self.validate_char(ch)
        try:
            return self.items.index(ch)
        except ValueError:
            return -1

    def findLast(self, ch):
        self.validate_char(ch)
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == ch:
                return i
        return -1

    def clear(self):
        self.items.clear()

    def extend(self, other):
        if not isinstance(other, ArrayList):
            raise TypeError("Expected ArrayList instance")
        self.items.extend(other.items.copy())

    def validate_char(self, c):
        if not isinstance(c, str) or len(c) != 1:
            raise ValueError("Element must be a single character")

    def __str__(self):
        return f"[{', '.join(self.items)}]"


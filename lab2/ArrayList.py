class ArrayList:
    def __init__(self):
        self._items = []

    def length(self):
        return len(self._items)

    def append(self, ch):
        if not isinstance(ch, str) or len(ch) != 1:
            raise ValueError("Only single characters allowed")
        self._items.append(ch)

    def delete(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("Index out of bounds")
        return self._items.pop(index)

    def insert(self, ch, index):
        if not isinstance(ch, str) or len(ch) != 1:
            raise ValueError("Only single characters allowed")
        if index < 0 or index > len(self._items):
            raise IndexError("Index out of bounds")
        self._items.insert(index, ch)

    def deleteAll(self, ch):
        self._items = [x for x in self._items if x != ch]

    def get(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("Index out of bounds")
        return self._items[index]

    def clone(self):
        copy = ArrayList()
        copy._data = self._items.copy()
        return copy

    def reverse(self):
        self._items.reverse()

    def findFirst(self, ch):
        try:
            return self._items.index(ch)
        except ValueError:
            return -1

    def findLast(self, ch):
        for i in range(len(self._items) - 1, -1, -1):
            if self._items[i] == ch:
                return i
        return -1

    def clear(self):
        self._items.clear()

    def extend(self, other):
        if not isinstance(other, ArrayList):
            raise TypeError("Expected ArrayList instance")
        self._items.extend(other._items.copy())

    def __str__(self):
        return f"[{', '.join(self._items)}]"


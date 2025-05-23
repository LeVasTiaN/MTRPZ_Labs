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

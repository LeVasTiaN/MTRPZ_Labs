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

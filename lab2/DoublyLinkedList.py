class DoublyLinkedListNode:
    def __init__(self, value: str):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def length(self) -> int:
        return self._length

    def append(self, element: str) -> None:
        self.validate_char(element)
        node = DoublyLinkedListNode(element)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self._length += 1

    def validate_char(self, c):
        if not isinstance(c, str) or len(c) != 1:
            raise ValueError("Element must be a single character")

    def insert(self, element: str, index: int) -> None:
        self.validate_char(element)
        if index < 0 or index > self._length:
            raise IndexError("Index out of range")

        new_node = DoublyLinkedListNode(element)

        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self._length == 0:
                self.tail = new_node
        elif index == self._length:
            self.append(element)
            return
        else:
            current = self._node_at(index)
            prev_node = current.prev
            new_node.next = current
            new_node.prev = prev_node
            if prev_node:
                prev_node.next = new_node
            current.prev = new_node

        self._length += 1

    def _node_at(self, index: int) -> DoublyLinkedListNode:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        if index < self._length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._length - 1, index, -1):
                current = current.prev
        return current

    def delete(self, index: int) -> str:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        current = self._node_at(index)

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

        self._length -= 1
        return current.value

    def deleteAll(self, element: str) -> None:
        self.validate_char(element)
        current = self.head
        while current:
            next_node = current.next
            if current.value == element:
                self._remove_node(current)
            current = next_node

    def _remove_node(self, node: DoublyLinkedListNode) -> None:
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        self._length -= 1

    def get(self, index: int) -> str:
        return self._node_at(index).value

    def clone(self):
        new_list = DoublyLinkedList()
        current = self.head
        while current:
            new_list.append(current.value)
            current = current.next
        return new_list

    def reverse(self) -> None:
        current = self.head
        self.tail = current
        prev_node = None
        while current:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
        self.head = prev_node

    def findFirst(self, element: str) -> int:
        self.validate_char(element)
        index = 0
        current = self.head
        while current:
            if current.value == element:
                return index
            current = current.next
            index += 1
        return -1

    def findLast(self, element: str) -> int:
        self.validate_char(element)
        index = self._length - 1
        current = self.tail
        while current:
            if current.value == element:
                return index
            current = current.prev
            index -= 1
        return -1

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self._length = 0

    def extend(self, other) -> None:
        if not isinstance(other, DoublyLinkedList):
            raise TypeError("Expected a DoublyLinkedList")
        current = other.head
        while current:
            self.append(current.value)
            current = current.next

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return f"[{', '.join(elements)}]"

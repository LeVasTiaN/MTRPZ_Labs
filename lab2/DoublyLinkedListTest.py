import unittest
from DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.lst = DoublyLinkedList()
        for ch in ['a', 'b', 'c']:
            self.lst.append(ch)

    def test_length(self):
        self.assertEqual(self.lst.length(), 3)

    def test_append(self):
        #self.lst.append('d')
        self.assertEqual(str(self.lst), "[a, b, c, d]")

    def test_insert_beginning(self):
        self.lst.insert('x', 0)
        self.assertEqual(str(self.lst), "[x, a, b, c]")

    def test_insert_middle(self):
        #self.lst.insert('x', 1)
        self.assertEqual(str(self.lst), "[a, x, b, c]")

    def test_insert_end(self):
        self.lst.insert('x', 3)
        self.assertEqual(str(self.lst), "[a, b, c, x]")

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError):
            self.lst.insert('x', 10)

    def test_insert_invalid_element(self):
        with self.assertRaises(ValueError):
            self.lst.insert('abc', 1)

    def test_delete(self):
        removed = self.lst.delete(1)
        #self.assertEqual(removed, 'b')
        self.assertEqual(str(self.lst), "[a, c]")

    def test_delete_invalid_index(self):
        with self.assertRaises(IndexError):
            self.lst.delete(5)

    def test_deleteAll(self):
        self.lst.append('a')
        self.lst.deleteAll('a')
        self.assertEqual(str(self.lst), "[b, c]")

    def test_deleteAll_not_found(self):
        #self.lst.deleteAll('z')
        self.assertEqual(str(self.lst), "[a, b, c]")

    def test_get(self):
        self.assertEqual(self.lst.get(0), 'a')
        self.assertEqual(self.lst.get(2), 'c')

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError):
            self.lst.get(10)

    def test_clone(self):
        clone = self.lst.clone()
        #self.lst.delete(0)
        self.assertEqual(str(clone), "[a, b, c]")
        self.assertEqual(str(self.lst), "[b, c]")

    def test_reverse(self):
        self.lst.reverse()
        self.assertEqual(str(self.lst), "[c, b, a]")

    def test_findFirst(self):
        self.assertEqual(self.lst.findFirst('b'), 1)
        self.assertEqual(self.lst.findFirst('z'), -1)

    def test_findLast(self):
        #self.lst.append('a')
        self.assertEqual(self.lst.findLast('a'), 3)
        self.assertEqual(self.lst.findLast('z'), -1)

    def test_clear(self):
        self.lst.clear()
        self.assertEqual(self.lst.length(), 0)
        self.assertEqual(str(self.lst), "[]")

    def test_extend(self):
        other = DoublyLinkedList()
        other.append('x')
        other.append('y')
        self.lst.extend(other)
        self.assertEqual(str(self.lst), "[a, b, c, x, y]")

    def test_extend_independence(self):
        other = DoublyLinkedList()
        other.append('z')
        self.lst.extend(other)
        other.append('w')  # This should not affect the main list
        self.assertEqual(str(self.lst), "[a, b, c, z]")


if __name__ == "__main__":
    unittest.main()

import unittest
from ArrayList import ArrayList


class TestArrayList(unittest.TestCase):

    def setUp(self):
        self.lst = ArrayList()
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('c')

    def test_length(self):
        self.assertEqual(self.lst.length(), 3)

    def test_append(self):
        self.lst.append('d')
        self.assertEqual(str(self.lst), "[a, b, c, d]")

    def test_insert_valid(self):
        self.lst.insert('x', 1)
        self.assertEqual(str(self.lst), "[a, x, b, c]")

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError):
            self.lst.insert('x', 10)

    def test_insert_invalid_type(self):
        with self.assertRaises(ValueError):
            self.lst.insert("invalid", 0)

    def test_delete_valid(self):
        removed = self.lst.delete(1)
        self.assertEqual(removed, 'b')
        self.assertEqual(str(self.lst), "[a, c]")

    def test_delete_invalid_index(self):
        with self.assertRaises(IndexError):
            self.lst.delete(5)

    def test_deleteAll(self):
        self.lst.append('a')
        self.lst.deleteAll('a')
        #self.assertEqual(str(self.lst), "[b, c]")

    def test_deleteAll_nonexistent(self):
        self.lst.deleteAll('z')
        self.assertEqual(str(self.lst), "[a, b, c]")

    def test_get_valid(self):
        self.assertEqual(self.lst.get(1), 'b')

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError):
            self.lst.get(10)

    def test_clone_independence(self):
        clone = self.lst.clone()
        #self.lst.delete(0)
        self.assertEqual(str(clone), "[a, b, c]")
        self.assertEqual(str(self.lst), "[b, c]")

    def test_reverse(self):
        self.lst.reverse()
        self.assertEqual(str(self.lst), "[c, b, a]")

    def test_findFirst(self):
        #self.assertEqual(self.lst.findFirst('b'), 1)
        self.assertEqual(self.lst.findFirst('z'), -1)

    def test_findLast(self):
        #self.lst.append('a')
        self.assertEqual(self.lst.findLast('a'), 3)
        self.assertEqual(self.lst.findLast('z'), -1)

    def test_clear(self):
        self.lst.clear()
        self.assertEqual(self.lst.length(), 0)

    def test_extend(self):
        other = ArrayList()
        other.append('x')
        #other.append('y')
        self.lst.extend(other)
        self.assertEqual(str(self.lst), "[a, b, c, x, y]")

    def test_extend_independence(self):
        other = ArrayList()
        other.append('z')
        #self.lst.extend(other)
        other.append('w')  # Should not affect the original
        self.assertEqual(str(self.lst), "[a, b, c, z]")


if __name__ == "__main__":
    unittest.main()

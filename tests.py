import unittest
from main import KDTree


class TestKDTInsert(unittest.TestCase):
    def test_kdt_int(self):
        length = 6
        arr = [(21, 12, 2), (10, 30, 43), (18, 8, 39), (3, 4, 9), (6, 70, 1), (8, 40, 33)]
        kdt = KDTree(3)

        for i in arr:
            kdt.insert(i)

        # Test insert & len
        self.assertEqual(len(kdt), length)

        # Test contains
        for value in arr:
            self.assertIn(value, kdt)

if __name__ == "__main__":
    unittest.main()

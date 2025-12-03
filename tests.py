import unittest
from main import KDTree


class TestKDTInt(unittest.TestCase):
    def test_kdt_int(self):
        arr = [[9, 12, 2], [10, 30, 43], [18, 8, 39], [3, 4, 9], [6, 70, 1], [8, 40, 33]]
        kdt = KDTree(3)

        for value in arr:
            kdt.insert(value)

        # Test insert & len
        self.assertEqual(len(kdt), len(arr))

        # Test contains
        for value in arr:
            self.assertIn(value, kdt)

        # Test delete
        arr = [[10, 30, 43], [18, 8, 39], [3, 4, 9], [6, 70, 1], [8, 40, 33]]

        kdt.delete([9, 12, 2])
        self.assertNotIn([9, 12, 2], kdt)
        self.assertEqual(len(kdt), len(arr))

        for value in arr:
            self.assertIn(value, kdt)

"""
class TestKDTString(unittest.TestCase):
    def test_kdt_string(self):
        arr = [["kiwi", "banana"], ["cranberry", "pineapple"], ["cheese", "pepperoni"], ["s'mores", "spinach"], ["onion", "tomato"]]
        kdt2 = KDTree(2)
        
        for value in arr:
            kdt2.insert(value)

        # Test insert & len
        self.assertEqual(len(kdt2), len(arr))

        # Test contains
        for value in arr:
            self.assertIn(value, kdt2)

        # Test delete
        arr = [["cranberry", "pineapple"], ["cheese", "pepperoni"], ["s'mores", "spinach"], ["onion", "tomato"]]

        kdt2.delete(["kiwi", "banana"])
        self.assertNotIn(["kiwi", "banana"], kdt2)
        self.assertEqual(len(kdt2), len(arr))

        for value in arr:
            self.assertIn(value, kdt2)
"""
if __name__ == "__main__":
    unittest.main()

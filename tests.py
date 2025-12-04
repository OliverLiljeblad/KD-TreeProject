import unittest
import random
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

        # Test nearest
        point, dist = kdt.nearest([3, 4, 5])
        self.assertEqual(point.value, [3, 4, 9])
        self.assertEqual(int(dist), 4)

        point, dist = kdt.nearest([100, 100, 100])
        self.assertEqual(point.value, [10, 30, 43])
        self.assertEqual(int(dist), 127)

        # Test delete
        arr = [[10, 30, 43], [18, 8, 39], [3, 4, 9], [6, 70, 1], [8, 40, 33]]

        kdt.delete([9, 12, 2])
        self.assertNotIn([9, 12, 2], kdt)
        self.assertEqual(len(kdt), len(arr))

        for value in arr:
            self.assertIn(value, kdt)


class TestKDTRandInt(unittest.TestCase):
    def test_kdt_rand__int(self):
        arr = []
        temp = []
        for i in range(100):
            for j in range(5):
                temp.append(random.randint(0, 100))
            arr.append(temp)
            temp = []
        
        arr2 = arr
        kdt = KDTree(5)

        for value in arr:
            kdt.insert(value)

        # Test insert & len
        self.assertEqual(len(kdt), len(arr))

        # Test contains
        for value in arr:
            self.assertIn(value, kdt)

        # Test delete
        for i in range(-20, 0, -1):
            temp = random.randint(0, len(arr2) - 20)
            kdt.delete(arr2[temp])
            arr2.pop(arr2[temp])
        
        self.assertEqual(len(kdt), len(arr2))
        for value in arr2:
            self.assertIn(value, kdt)


if __name__ == "__main__":
    unittest.main()
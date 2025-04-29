import unittest
from src.data_structures.sets import add_to_set, remove_from_set, set_operations

class TestSetOperations(unittest.TestCase):

    def setUp(self):
        self.test_set = {1, 2, 3}
        self.another_set = {3, 4, 5}

    def test_add_to_set(self):
        result = add_to_set(self.test_set, 4)
        self.assertIn(4, result)

    def test_remove_from_set(self):
        result = remove_from_set(self.test_set, 2)
        self.assertNotIn(2, result)

    def test_set_operations_union(self):
        result = set_operations(self.test_set, self.another_set, operation='union')
        expected = {1, 2, 3, 4, 5}
        self.assertEqual(result, expected)

    def test_set_operations_intersection(self):
        result = set_operations(self.test_set, self.another_set, operation='intersection')
        expected = {3}
        self.assertEqual(result, expected)

    def test_set_operations_difference(self):
        result = set_operations(self.test_set, self.another_set, operation='difference')
        expected = {1, 2}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
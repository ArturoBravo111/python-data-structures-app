import unittest
from src.data_structures.lists import add_element, remove_element, iterate_list

class TestListOperations(unittest.TestCase):

    def setUp(self):
        self.test_list = [1, 2, 3]

    def test_add_element(self):
        result = add_element(self.test_list, 4)
        self.assertIn(4, result)

    def test_remove_element(self):
        result = remove_element(self.test_list, 2)
        self.assertNotIn(2, result)

    def test_iterate_list(self):
        result = list(iterate_list(self.test_list))
        self.assertEqual(result, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
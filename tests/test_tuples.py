import unittest
from src.data_structures.tuples import create_tuple, access_element

class TestTuples(unittest.TestCase):

    def test_create_tuple(self):
        expected = (1, 2, 3)
        result = create_tuple(1, 2, 3)
        self.assertEqual(result, expected)

    def test_access_element(self):
        sample_tuple = (10, 20, 30)
        result = access_element(sample_tuple, 1)
        self.assertEqual(result, 20)

        with self.assertRaises(IndexError):
            access_element(sample_tuple, 5)

if __name__ == '__main__':
    unittest.main()
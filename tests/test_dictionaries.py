import unittest
from src.data_structures.dictionaries import add_entry, remove_entry, get_value

class TestDictionaries(unittest.TestCase):

    def setUp(self):
        self.test_dict = {}

    def test_add_entry(self):
        add_entry(self.test_dict, 'key1', 'value1')
        self.assertEqual(self.test_dict['key1'], 'value1')

    def test_remove_entry(self):
        add_entry(self.test_dict, 'key2', 'value2')
        remove_entry(self.test_dict, 'key2')
        self.assertNotIn('key2', self.test_dict)

    def test_get_value(self):
        add_entry(self.test_dict, 'key3', 'value3')
        value = get_value(self.test_dict, 'key3')
        self.assertEqual(value, 'value3')

    def test_get_nonexistent_value(self):
        value = get_value(self.test_dict, 'nonexistent_key')
        self.assertIsNone(value)

if __name__ == '__main__':
    unittest.main()
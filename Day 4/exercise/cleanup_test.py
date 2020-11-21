from modules.cleanup import Cleanup
import unittest

class TestCleanup(unittest.TestCase):

    def setUp(self):
        self.data = {'city':'Budapest', 'country':'Hun'}

    def test_cleanup(self):      
        cleaned = Cleanup.cleanup(**self.data)
        self.assertEqual(cleaned, ({'city':'budapest', 'country': 'hun'}))

    def test_cleanup_with_no_city(self):
        cleaned = Cleanup.cleanup(city='', country='swe')
        self.assertEqual(cleaned, ({'city':'edinburgh', 'country':'swe'}))


if __name__ == '__main__':
    unittest.main()
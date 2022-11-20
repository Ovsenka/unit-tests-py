import unittest

class TestCase(unittest.TestCase):
    def setUp(self):
        print("Start", self)
    def tearDown(self):
        print("Stop", self)
    def test_equal(self):
        self.assertEqual(3*4, 12)
        self.assertEqual('v' * 4, 'vvvv')
    def test_bool(self):
        self.assertTrue(not False, True)
        self.assertTrue("aaa", "aaa")    
    
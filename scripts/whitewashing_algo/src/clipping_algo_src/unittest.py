import os
import unittest
from read_image_info import read_info

class TestLocation(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_location(self):
        self.assertEqual(1,os.path.exists("D:\\Dropbox\\ankur\\pixel_tests\\test.png"))
        
if __name__ == '__main__':
    unittest.main()
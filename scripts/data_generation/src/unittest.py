import os
import unittest
from batch_resize import batch_resize

class TestLocation(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_location(self):
        self.assertEqual(1,os.path.exists("Desktop"))
        
if __name__ == '__main__':
    unittest.main()
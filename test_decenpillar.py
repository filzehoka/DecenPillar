# test_decenpillar.py
"""
Tests for DecenPillar module.
"""

import unittest
from decenpillar import DecenPillar

class TestDecenPillar(unittest.TestCase):
    """Test cases for DecenPillar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DecenPillar()
        self.assertIsInstance(instance, DecenPillar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DecenPillar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

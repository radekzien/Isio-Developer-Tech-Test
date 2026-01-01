import sys
from pathlib import Path

# Add parent directory to path so imports work when running this file directly
sys.path.insert(0, str(Path(__file__).parent.parent))

import unittest

from gilded_rose import GildedRose
from item_classes import *


class GildedRoseTest(unittest.TestCase):
    def test_Item(self):
        """
        Checks for correct instantiaton of Item Class
        """
        items = [Item("Example Item", 10, 2)]
        self.assertEqual("Example Item", items[0].name)
        self.assertEqual(2, items[0].quality)
        self.assertEqual(10, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()

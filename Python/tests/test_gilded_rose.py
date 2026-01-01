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

    def test_RegularItemLogic(self):
        """
        Checks for correct quality and sell_in logic for RegularItem
        """
        items = [RegularItem("Regular Item", 10, 10), RegularItem("Expired Item", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 10 - items[0].degrade_value)
        self.assertEqual(items[1].sell_in, 9)
        self.assertEqual(items[1].quality, 10 - (items[0].degrade_value * 2))

    def test_AgingItemLogic(self):
        """
        Checks for correct quality and sell_in logic for AgingItem
        """
        items = [AgingItem("Example Item", 10, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 3)

    def test_LegendaryItemLogic(self):
        """
        Checks for correct quality and sell_in logic for LegendaryItem
        """
        items = [LegendaryItem("Example Item", 10, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 10)
        self.assertEqual(items[0].quality, 2)

    def test_BackstageItemLogic(self):
        """
        Checks for correct quality and sell_in logic for BackstageItem
        """
        items = [BackstageItem("over10", 12, 5), BackstageItem("under10", 10, 5), BackstageItem("under5", 5, 5), BackstageItem("afterConcert", -1, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 11)
        self.assertEqual(items[0].quality, 6)
        self.assertEqual(items[1].sell_in, 9)
        self.assertEqual(items[1].quality, 7)
        self.assertEqual(items[2].sell_in, 4)
        self.assertEqual(items[2].quality, 8)
        self.assertEqual(items[3].sell_in, -2)
        self.assertEqual(items[3].quality, 0)

    def test_ConjuredItemLogic(self):
        """
        Checks for correct quality and sell_in logic for ConjuredItem
        """
        items = [ConjuredItem("Regular Item", 10, 10), ConjuredItem("Expired Item", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 10 - items[0].degrade_value)
        self.assertEqual(items[1].sell_in, 9)
        self.assertEqual(items[1].quality, 10 - (items[0].degrade_value * 2))

if __name__ == '__main__':
    unittest.main()

QUALITY_MAX = 50
QUALITY_MIN = 0

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class RegularItem(Item): #Regular items - degrade in quality by 1, degrade twice as fast after sell by date
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
        self.degrade_value = 1

    def update_quality(self):
        if self.quality > QUALITY_MIN:
            self.quality -= self.degrade_value
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality -= self.degrade_value

class AgingItem(Item): #Aging item - increases in quality the older it gets up to 50
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality(self):
        if self.quality < QUALITY_MAX:
            self.quality += 1
        self.sell_in -= 1

class LegendaryItem(Item): #Legendary Item - Never sold or decreases in quality
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality(self):
        pass

class BackstageItem(Item): #Bacstage item - Quality increases by 2 10 days before concert, or by 3 5 days before concert, but worthless after the concert
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality(self):
        if self.sell_in <= 10 and self.sell_in > 5:
            self.quality += 2
        elif self.sell_in <= 5:
            self.quality += 3
        if self.sell_in < 0:
            self.quality = 0
        self.sell_in -= 1

class ConjuredItem(RegularItem): #Conjured item - Subclass of Regular Item - "Conjured items degrade in Quality twice as fast as normal items"
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
        self.degrade_value *=2
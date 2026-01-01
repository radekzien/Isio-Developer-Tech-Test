class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class RegularItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.quality > 0:
            self.quality -= 1
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality -=1

class AgingItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
        self.sell_in -= 1

class LegendaryItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality(self):
        pass

class BackstageItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality(self):
        if self.sell_in <= 10 and self.sell_in > 5:
            self.quality += 2
        elif self.sell_in <= 5:
            self.quality += 3
        if self.sell_in <= 0:
            self.quality = 0
        self.sell_in -= 1
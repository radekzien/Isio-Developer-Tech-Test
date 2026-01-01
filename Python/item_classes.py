#--- QUALITY CONSTRAINTS ---
QUALITY_MAX = 50
QUALITY_MIN = 0

#--- ITEM CLASSES ---
class Item:
    """
    Original Item class, unchanged from original assignment
    """
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class RegularItem(Item):
    """
    RegularItem: Subclass of Item
        Represents normal items
            - Degrade in quality by 1
            - Degrade twice as fast after sell by date
    """
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
        self.degrade_value = 1 #Made as an explicit variable so it can be changed/manipulated by subclasses

    def update_quality(self):
        self.quality -= self.degrade_value
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality -= self.degrade_value #Degrades a second time if past sellby date
        self.quality = max(self.quality, QUALITY_MIN)

class AgingItem(Item):
    """
    AgingItem: Subclass of Item
        Represents items that increase in quality with age
            - Increases in quality the older it gets up to MAX_QUALITY
    """
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality(self):
        self.quality += 1
        self.sell_in -= 1
        self.quality = min(self.quality, QUALITY_MAX)

class LegendaryItem(Item):
    """
    LegendaryItem: Subclass of Item
        Represents items that are never sold or decrease in quality
    """
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality(self):
       self.quality = min(self.quality, QUALITY_MAX) #Enforces quality constraint

class BackstageItem(Item):
    """
    BackstageItem: Subclass of Item
        Represents items such as Backstage passes that increase in quality until the sell_in date
            - Quality increase by 2 for up to 10 days before the concert
            - Quality increases by 3 for up to 5 days before the concert
            - Quality set to 0 following the concert (Days following instead of day of as it may still hold value
            day of the concert, similar to how people sell their concert tickets on the day of the concert. Assignment
            uses keyword 'after'.)
    """
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0: #Less than instead of <= because assumed value still holds day of the concert
            self.quality = 0
        else:
            if self.sell_in <= 10 and self.sell_in > 5:
                self.quality += 2
            elif self.sell_in <= 5:
                self.quality += 3
        self.quality = min(self.quality, QUALITY_MAX)

class ConjuredItem(RegularItem):
    """
    ConjuredItem: Subclass of regular item
        Represents new type of item
            - Degrade twice as fast as normal items
    """
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
        self.degrade_value *=2 #Double the degrade_value for regular items
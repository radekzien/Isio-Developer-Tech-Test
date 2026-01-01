# Gilded Rose starting position in Python

For exercise instructions see [top level README](../README.md)

## Running the unit tests from the Command-Line

```
python -m unittest
```

## Running the example simulation from the Command-Line

For e.g. 10 days:

```
python example_simulation.py 10
```
# Participant Notes
## Classes and Inheritance
The first thing that struck me in the original codebase was the excessive amount of checks under the update_quality() function. String equality checks meant that in the future, should Gilded Rose add new items that share qualities to existing items, their names would have to be added to existing if statements which would become a nightmare for readability and maintainability. The best solution for this was to create subclasses of the class Item that reflect the qualities shown in the codebase and the assignment. This lead to the creation of item_classes.py where I created a subclass of the parent class Item for each of the desired item types.

## Conjured Item feature
Gilded Rose described a new item type, which decreases in quality twice as fast as regular items: Conjured Items. I created this as a subclass of RegularItems, as the behaviour is almost identical except for the doubled expiry rate. Both RegularItems and ConjuredItems have a degrade_value which dictates how much the item decreases in quality each day. The degrade_value for ConjuredItems is 2x the degrade value for RegularItems, and is initialised as such. Treating ConjuredItem as a subclass of RegularItem improves readability and maintability in code.

## MAX_QUALITY and MIN_QUALITY
Should the behaviour of items change in the future, these two values can be changed instead of going through the whole codebase. This improves maintainability for both testing and development.

## Tests
The unit test tests the quality logic of each class. They also test whether the relevant classes respect quality constraints after both a single iteration, and multiple iterations.

## Additional notes
  - min() and max() were used to enforce quality value constraints instead of if statements to reduce the amount of code and improve readability.
  - Decrementing sell_in was moved to the start of each update_quality() function to ensure correct behavior according to the assignment rules. For example, sell_in = 0 indicates the item is due today. If we looked at a BackstageItem, its quality remains above 0 until sell_in becomes -1, which represents that the day has passed.

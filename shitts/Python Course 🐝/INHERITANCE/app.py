from chef import Chef
from chineesechef import ChineseeChef

# Use the ChineseeChef subclass (overrides `Chef` methods)
mychef = ChineseeChef()
mychef.make_chicken()
mychef.make_salad()
mychef.make_special_dish()
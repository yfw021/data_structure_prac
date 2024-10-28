class Bag(object):

    def __init__(self,maxsize = 10):
        self.maxsize = maxsize
        self._items = list()

    def add(self, item):
        if len(self) > self.maxsize:
            raise Exception('Bag is full')
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        for item in self._items:
            yield item
    
def test_bag():
    bag = Bag()
    bag.add(1)
    bag.add(2)
    bag.add(3)
    bag.add(4)
    bag.add(5)

    assert len(bag) == 5 # the bag has 5 items
    bag.remove(3) # remove item 3
    assert len(bag) == 4 # the bag has 4 items

    for i in bag:
         print(i)
    print('test done')

test_bag()


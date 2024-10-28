class Array(object):
    def __init__(self, size = 32): # size = 32 is the default size
        self._size = size
        self._items = [None] * size # create a list of size 32 with None values

    def __getitem__(self, index): # get the value of the index
        return self._items[index] 

    def __setitem__(self, index, value):   # set the value of the index
        self._items[index] = value

    def __len__(self): # return the length of the list
        return self._size

    def clear(self, value = None): # clear the list
        for i in range(len(self._items)): # iterate through the list
            self._items[i] = value

    def __iter__(self): # iterate through the list
        for item in self._items:
            yield item

def test_array():
    size = 10
    a = Array(size)
    a[0] = 1 # set the value of the index 0 to 1
    print(a[0]) # get the value of the index 0
    assert a[0] == 1 # check if the value of the index 0 is 1
    assert len(a) == size # check if the length of the list is 10
    a.clear() # clear the list
    assert a[0] == None # check if the value of the index 0 is None
    a[0] = 1
    a[1] = 2
    a[2] = 3
    a[3] = 4
    a[4] = 5
    a[5] = 6
    for i in a:
        print(i)
    
    print("test_array passed")
    
test_array()
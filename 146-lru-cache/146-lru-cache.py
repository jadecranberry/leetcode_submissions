# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#popitem(last=True)
#The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are #returned in LIFO order if last is true or FIFO order if false.

#move_to_end(key, last=True)
#Move an existing key to either end of an ordered dictionary. The item is moved to the right end if last #is true (the default) or to the beginning if last is false. Raises KeyError if the key does not exist:

from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1;
        #cause we remove the item FIFO, so move the item to the end if we use it more frequently so that we can push the not frequent item to the top.
        self.move_to_end(key)
        return self[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value    
        if len(self) > self.capacity:
            self.popitem(last = False)
        
        
            



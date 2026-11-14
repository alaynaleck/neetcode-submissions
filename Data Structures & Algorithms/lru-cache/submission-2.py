class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.oldest = ListNode(0, 0)
        self.newest = ListNode(0, 0)
        self.cache = {}

        self.oldest.next, self.newest.prev = self.newest, self.oldest

    def add(self, node: ListNode):
        prev, nxt = self.newest.prev, self.newest
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def remove(self, node: ListNode):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int):
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]
        



            

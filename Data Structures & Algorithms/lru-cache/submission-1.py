
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.last = ListNode(None, None)
        self.first = ListNode(None, None)
        self.first.prev, self.last.next = self.last, self.first

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def add(self, node):
        prev, nxt = self.first.prev, self.first
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.last.next
            self.remove(lru)
            del self.cache[lru.key]

            

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.tail.next = self.head
        self.head.prev = self.tail

    def remove(self, node):
        prev = node.prev
        nxt =  node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.head.prev
        nxt =  self.head
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.tail.next
            self.remove(lru)
            del self.cache[lru.key]
        

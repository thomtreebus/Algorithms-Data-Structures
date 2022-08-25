class ListNode:
    def __init__(self, key, value, nxt):
        self.key = key
        self.value = value
        self.next = nxt
        
class MyHashMap:
    def __init__(self):
        self.size = 19997
        self.mult = 12582917
        self.data = [None for i in range(self.size)]
        
    def hash(self, key):
        return key * self.mult % self.size

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        h = self.hash(key)
        node = ListNode(key, value, self.data[h])
        self.data[h] = node
        
    def get(self, key: int) -> int:
        h = self.hash(key)
        node = self.data[h]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        node = self.data[h]
        if not node:
            return
        if node.key == key:
            self.data[h] = node.next
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next
class Node:
    
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.mp = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self, node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.mp: return -1
        
        node = self.mp[key]
        self.pop(node)
        self.append(node)
        
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            self.pop(node)
            node.value = value
            self.append(node)
        else:
            if self.size == self.capacity:
                node = self.pop()
                del self.mp[node.key]
                self.size -= 1
                
            node = Node(key, value)
            self.mp[key] = node
            self.append(node)
            self.size += 1
            
    def pop(self, node = None):
        if not node:
            node = self.tail.prev
        
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
        return node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
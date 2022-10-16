class Node:
    
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DLinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def append(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
        self.size += 1
    
    def pop(self, node = None):
        if self.size == 0: return

        if not node:
            node = self.tail.prev
        
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
        self.size -= 1
        
        return node
    
class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.mp = dict()
        self.minFreq = 0
        self.freq = collections.defaultdict(DLinkedList)
    
    def _update(self, node):
        freq = node.freq
        
        self.freq[freq].pop(node)
        if self.minFreq == freq and not self.freq[freq]:
            self.minFreq += 1
            
        node.freq += 1
        freq = node.freq
        self.freq[freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.mp: return -1
        
        node = self.mp[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        
        if key in self.mp:
            node = self.mp[key]
            node.value = value
            self._update(node)
        else:
            if self.size == self.capacity:
                node = self.freq[self.minFreq].pop()
                del self.mp[node.key]
                self.size -= 1
            
            node = Node(key, value)
            self.mp[key] = node
            self.freq[1].append(node)
            self.minFreq = 1
            self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
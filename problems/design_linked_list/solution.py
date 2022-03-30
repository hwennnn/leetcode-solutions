class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size or not self.head: return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        curr = self.head
        
        if not curr:
            self.head = Node(val)
        else:
            while curr.next:
                curr = curr.next
            curr.next = Node(val)

        self.size += 1
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
        
        if not (0 <= index < self.size): return
        
        node = Node(val)
        curr = self.head
        
        for _ in range(index - 1):
            curr = curr.next
        
        nxt = curr.next
        curr.next = None
        node.next = nxt
        curr.next = node
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        
        if not (0 <= index < self.size): return
        
        curr = self.head
        
        for _ in range(index - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
---
id: linked-list-random-node
title: Linked List Random Node
description: Problem Description and Solution for Linked List Random Node
sidebar_label: 382. Linked List Random Node
sidebar_position: 382
---

# [382. Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/)

```py title=linked-list-random-node.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.A = []
        self.n = 0
        
        curr = head
        while curr:
            self.A.append(curr.val)
            curr = curr.next
            self.n += 1

    def getRandom(self) -> int:
        n = random.randint(0, self.n - 1)
        
        return self.A[n]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

```cpp title=linked-list-random-node.cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
    vector<int> v;
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        while (head){
            v.push_back(head->val);
            head = head->next;
        }
        srand(time(0));
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        int r = rand() % v.size();
        return v[r];
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
```



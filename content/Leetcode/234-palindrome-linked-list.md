---
title: 234. Palindrome Linked List
draft: false
tags: 
  - leetcode-easy
  - linked-list
  - two-pointers
  - stack
  - recursion
date: 2020-12-13
---

[Problem Link](https://leetcode.com/problems/palindrome-linked-list/)

## Description

---
<p>Given the <code>head</code> of a singly linked list, return <code>true</code><em> if it is a </em><span data-keyword="palindrome-sequence"><em>palindrome</em></span><em> or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg" style="width: 422px; height: 62px;" />
<pre>
<strong>Input:</strong> head = [1,2,2,1]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg" style="width: 182px; height: 62px;" />
<pre>
<strong>Input:</strong> head = [1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you do it in <code>O(n)</code> time and <code>O(1)</code> space?

## Solution

---
### Python
``` py title='palindrome-linked-list'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # 1) move slow pointer to the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        def reverseLL(curr):
            prev = None

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            return prev

        # 2) reverse the second half of the linked list
        rhead = reverseLL(slow)

        # 3) compare the first half and the reversed second half
        while rhead:
            if head.val != rhead.val:
                return False
            
            head = head.next
            rhead = rhead.next
        
        return True
```
### C++
``` cpp title='palindrome-linked-list'
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
public:
    bool isPalindrome(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return true;
        
        ListNode *slow = head, *fast = head;
        
        while (fast->next && fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        
        slow->next = reverseLL(slow->next);
        slow = slow->next;
        
        while (slow){
            if (head->val != slow->val) return false;
            
            head = head->next;
            slow = slow->next;
        }
        
        return true;
        
    }
    
    ListNode* reverseLL(ListNode *node){
        ListNode *res = NULL;
        
        while (node){
            ListNode *next = node->next;
            node->next = res;
            res = node;
            node = next;
        }
        
        return res;
    }
};
```


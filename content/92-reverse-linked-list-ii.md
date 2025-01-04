---
title: 92. Reverse Linked List II
draft: false
tags: 
  - leetcode-medium
  - linked-list
date: 2020-12-11
---

[Problem Link](https://leetcode.com/problems/reverse-linked-list-ii/)

## Description

---
<p>Given the <code>head</code> of a singly linked list and two integers <code>left</code> and <code>right</code> where <code>left &lt;= right</code>, reverse the nodes of the list from position <code>left</code> to position <code>right</code>, and return <em>the reversed list</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], left = 2, right = 4
<strong>Output:</strong> [1,4,3,2,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [5], left = 1, right = 1
<strong>Output:</strong> [5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>n</code>.</li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>-500 &lt;= Node.val &lt;= 500</code></li>
	<li><code>1 &lt;= left &lt;= right &lt;= n</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you do it in one pass?

## Solution

---
### Python
``` py title='reverse-linked-list-ii'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr, prev = head, dummy

        for _ in range(left - 1):
            prev = prev.next
            curr = curr.next
        
        A = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = A
            A = curr
            curr = nxt
        
        prev.next.next = curr
        prev.next = A

        return dummy.next


```
### C++
``` cpp title='reverse-linked-list-ii'
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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (m == n) return head;
        
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        
        ListNode *curr = head, *prev = dummy;
        
        for (int i = 0; i < m - 1; i++){
            curr = curr->next;
            prev = prev->next;
        }
        
        ListNode *temp = NULL;
        for (int i = 0; i < n-m+1; i++){
            ListNode* next = curr->next;
            curr->next = temp;
            temp = curr;
            curr = next;
        }
        
        prev->next->next = curr;
        prev->next = temp;
        
        return dummy->next;
    }
};
```


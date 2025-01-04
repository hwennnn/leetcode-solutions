---
title: 82. Remove Duplicates from Sorted List II
draft: false
tags: 
  - leetcode-medium
  - linked-list
  - two-pointers
date: 2022-03-09
---

[Problem Link](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## Description

---
<p>Given the <code>head</code> of a sorted linked list, <em>delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list</em>. Return <em>the linked list <strong>sorted</strong> as well</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg" style="width: 500px; height: 142px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,3,4,4,5]
<strong>Output:</strong> [1,2,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg" style="width: 500px; height: 205px;" />
<pre>
<strong>Input:</strong> head = [1,1,1,2,3]
<strong>Output:</strong> [2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 300]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li>The list is guaranteed to be <strong>sorted</strong> in ascending order.</li>
</ul>


## Solution

---
### Python3
``` py title='remove-duplicates-from-sorted-list-ii'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = res = ListNode(-1, head)
        
        while curr:
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                v = curr.next.val
                p = curr.next
                
                while p and p.val == v:
                    p = p.next
                
                curr.next = p
            else:
                curr = curr.next
        
        return res.next
```


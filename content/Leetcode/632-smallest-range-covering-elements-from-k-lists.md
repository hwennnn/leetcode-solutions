---
title: 632. Smallest Range Covering Elements from K Lists
draft: false
tags: 
  - array
  - hash-table
  - greedy
  - sliding-window
  - sorting
  - heap-(priority-queue)
date: 2024-10-13
---

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-blue.svg)

## Description

---
<p>You have <code>k</code> lists of sorted integers in <strong>non-decreasing&nbsp;order</strong>. Find the <b>smallest</b> range that includes at least one number from each of the <code>k</code> lists.</p>

<p>We define the range <code>[a, b]</code> is smaller than range <code>[c, d]</code> if <code>b - a &lt; d - c</code> <strong>or</strong> <code>a &lt; c</code> if <code>b - a == d - c</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
<strong>Output:</strong> [20,24]
<strong>Explanation: </strong>
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [[1,2,3],[1,2,3],[1,2,3]]
<strong>Output:</strong> [1,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums.length == k</code></li>
	<li><code>1 &lt;= k &lt;= 3500</code></li>
	<li><code>1 &lt;= nums[i].length &lt;= 50</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i][j] &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code>&nbsp;is sorted in <strong>non-decreasing</strong> order.</li>
</ul>


## Solution

---
### Python
``` py title='smallest-range-covering-elements-from-k-lists'
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Min-heap to track the smallest element across all lists
        min_heap = []
        current_max = float('-inf')  # Track the current largest element in the window
        
        # Initialize the heap with the first element from each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))  # (value, list_index, element_index)
            current_max = max(current_max, nums[i][0])  # Update the max value
        
        # Initialize the result range to a very large one
        result_range = [-10**5, 10**5]
        
        while min_heap:
            current_min, list_idx, elem_idx = heapq.heappop(min_heap)  # Pop the smallest element
            
            # Check if the current range [current_min, current_max] is smaller
            if current_max - current_min < result_range[1] - result_range[0]:
                result_range = [current_min, current_max]
            
            # If we have reached the end of one of the lists, break the loop
            if elem_idx + 1 == len(nums[list_idx]):
                break
            
            # Otherwise, push the next element from the same list into the heap
            next_elem = nums[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_elem, list_idx, elem_idx + 1))
            
            # Update the max value
            current_max = max(current_max, next_elem)
        
        return result_range

```


---
title: Binary Search
tags:
  - algorithms
  - binary-search
  - search
date: 2023-11-14
---

## Introduction

**Binary Search** is a powerful searching algorithm that works by repeatedly dividing the search space in half. The core idea is simple - at each step, we look at the middle element and eliminate half of the remaining search space that cannot possibly contain our target. This process continues until we either find the target or determine it doesn't exist.

For example, when searching for a number in a sorted array, we compare our target with the middle element. If the target is smaller, we can safely discard the entire right half since all elements there would be too large. Similarly, if the target is larger, we discard the left half. By eliminating half the possibilities in each step, we reduce the search time from $O(n)$ to $O(\log n)$.

The algorithm requires the data to be sorted, which may take $O(n \log n)$ time initially. However, once sorted, all subsequent binary searches will be very efficient, especially for large datasets where the $O(\log n)$ time complexity really shines compared to linear $O(n)$ search.

Binary search isn't limited to just finding specific values - it can also be used to find **minimum** or **maximum** values that satisfy certain conditions in a search space.

## Implementation

### Searching minimum

```py
while left < right:
    mid = (left + right) // 2

    if good(mid):
        right = mid
    else:
        left = mid + 1

return left
```

### Searching maximum

```py
while left < right:
    mid = (left + right + 1) // 2

    if good(mid):
        left = mid
    else:
        right = mid - 1

return left
```

## Complexity

- Time complexity: $O(\log n)$ for the search function
- Space complexity: ${O(1)}$

## Resources

1. [Python Powerful Ultimate Binary Search Template - LeetCode](https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems)

---
title: Ternary Search
tags:
  - algorithms
  - search
  - ternary-search
date: 2024-05-06
---

## Introduction

**Ternary Search** is an algorithm to find the minimum or maximum of a unimodal function. In [[Binary Search]], the array is divided into two parts while in [[Ternary Search]], the array is divided into three parts.

## Implementation

### Searching minimum

```py
while left <= right:
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    if cost(mid1) <= cost(mid2):
        right = mid2 - 1
    else:
        left = mid1 + 1

return left
```

### Searching maximum

```py
while left <= right:
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    if cost(mid1) >= cost(mid2):
        right = mid2 - 1
    else:
        left = mid1 + 1

return left
```

## Complexity

- Time complexity: $O(\log n)$ for the search function
- Space complexity: ${O(1)}$

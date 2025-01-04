---
title: Monotonic Stack
tags:
  - data-structures
  - stack
date: 2023-12-01
---

## Introduction

A monotonic stack is a stack that maintains the elements in a way that preserves their monotonic order. Monotonic stacks are often used in problems that require finding the next greater or smaller element for each element in an array in ${O(n)}$ time.

## Implementation

### A generic template

```python
stack = []

for i, x in enumerate(arr):
    while stack and stack[-1] 'OPERATOR' x:
        // if the previous condition is satisfied, we pop the top element
        stackTop = stack.pop()

        // nextGreater[stackTop] = i

    if stack:
        // prevGreater[i] = stackTop

    stack.append(i)
```

![[monotonic-stack.png]]

### Find next greater element

```python
N = len(arr)
stack = []
nextGreater = [-1] * N

for i, x in enumerate(arr):
    // maintain decreasing monotonic stack
    while stack and x > arr[stack[-1]]:
        stackTop = stack.pop()

        nextGreater[stackTop] = i

    stack.append(i)
```

### Find previous greater element

```python
N = len(arr)
stack = []
prevGreater = [-1] * N

for i, x in enumerate(arr):
    // maintain decreasing monotonic stack
    while stack and x >= arr[stack[-1]]:
        stack.pop()

    if stack:
        prevGreater[i] = stack[-1]

    stack.append(i)
```

### Find next smaller element

```python
N = len(arr)
stack = []
nextSmaller = [-1] * N

for i, x in enumerate(arr):
    // maintain increasing monotonic stack
    while stack and x < arr[stack[-1]]:
        stackTop = stack.pop()

        nextSmaller[stackTop] = i

    stack.append(i)
```

### Find previous smaller element

```python
N = len(arr)
stack = []
prevSmaller = [-1] * N

for i, x in enumerate(arr):
    // maintain increasing monotonic stack
    while stack and x <= arr[stack[-1]]:
        stackTop = stack.pop()

    if stack:
        prevSmaller[i] = stack[-1]

    stack.append(i)
```

Summary

| Problem          | Stack Type                 | Operator in while loop | Assignment Position |
| ---------------- | -------------------------- | ---------------------- | ------------------- |
| next greater     | decreasing (equal allowed) | stackTop < current     | inside while loop   |
| previous greater | decreasing (strict)        | stackTop <= current    | outside while loop  |
| next smaller     | increasing (equal allowed) | stackTop > current     | inside while loop   |
| previous smaller | increasing (strict)        | stackTop >= current    | outside while loop  |

- next greater decreasing (equal allowed) `stackTop < current` inside while loop
- previous greater decreasing (strict) `stackTop <= current` outside while loop
- next smaller increasing (equal allowed) `stackTop > current` inside while loop
- previous smaller increasing (strict) `stackTop >= current` outside while loop

## Complexity

- Time complexity: ${O(n)}$
- Space complexity: ${O(n)}$

## Resources

1. [A comprehensive guide and template for monotonic stack based problems](https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems)

---
title: Combinatorics
tags:
  - math
  - combinatorics
date: 2023-10-22
---

## Count number of subarrays containing an element

Let's say we have an array `[1, 2, 3, 4]`,
count the number of subsequences containing element 3.

The formula is **`(i + 1) * (N - i)`**.

On the left of element 3 (inclusive of 3), you have `[1]`, `[1, 2]`, and `[1, 2, 3]`, which are three subsequences.

On the right of element 3, you have `[]` (empty subsequence) and `[4]`, which are two subsequences.

Multiplying the choices on the left and the right gives the total count: `3 * 2 = 6`.

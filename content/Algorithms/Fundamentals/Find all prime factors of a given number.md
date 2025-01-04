---
title: Find all prime factors of a given number
tags:
  - algorithms
  - math
  - prime-factors
date: 2023-10-22
---

## Introduction

## Implementation

```py
def primeFactors(n):
    factors = []

    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i

    if n > 2:
        factors.append(n)

    return factors
```

## Complexity

- Time complexity: $O(\sqrt(n))$
- Space complexity: $O(1)$

## Resources

1. [Print all prime factors of a given number - GeeksforGeeks](https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/)

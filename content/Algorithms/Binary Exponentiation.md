---
title: Binary Exponentiation
tags:
  - algorithms
  - math
date: 2023-10-22
---

## Introduction

Binary exponentiation (also known as exponentiation by squaring) is a trick which allows to calculate $a^n$ using only $O(\log n)$ multiplications (instead of $O(n)$ multiplications required by the naive approach).

The following recursive approach expresses the same idea:

$$
a^n = \begin{cases}
1 &\text{if } n == 0 \\
\left(a^{\frac{n}{2}}\right)^2 &\text{if } n > 0 \text{ and } n \text{ even}\\
\left(a^{\frac{n - 1}{2}}\right)^2 \cdot a &\text{if } n > 0 \text{ and } n \text{ odd}\\
\end{cases}
$$

## Implementation

### Recursive

```py
def binpow(a, b):
    if b == 0: return 1

    res = binpow(a, b // 2)
    if b % 2 == 0:
        return res * res
    else:
        return res * res * a
```

### Iterative

```py
def binpow(a, b):
    res = 1

    while b > 0:
        if b & 1:
            res *= a

        a *= a
        b >>= 1

    return res
```

## Complexity

- Time complexity: $O(\log n)$
- Space complexity: $O(1)$

## Resources

1. [Binary Exponentiation - CP Algorithm](https://cp-algorithms.com/algebra/binary-exp.html)

---
title: Euclidean Algorithm
tags:
  - algorithms
  - math
  - gcd
  - lcm
date: 2023-10-22
---

## What is GCD?

**Greatest common divisor** (GCD) is the largest number which is a divisor of both $a$ and $b$. It's commonly denoted by $\gcd(a, b)$.

## Algorithm

Originally, the Euclidean algorithm was formulated as follows: subtract the smaller number from the larger one until one of the numbers is zero. Indeed, if $g$ divides $a$ and $b$, it also divides $a-b$. On the other hand, if $g$ divides $a-b$ and $b$, then it also divides $a = b + (a-b)$, which means that the sets of the common divisors of $\{a, b\}$ and $\{b,a-b\}$ coincide.

Note that $a$ remains the larger number until $b$ is subtracted from it at least $\left\lfloor\frac{a}{b}\right\rfloor$ times. Therefore, to speed things up, $a-b$ is substituted with $a-\left\lfloor\frac{a}{b}\right\rfloor b = a \bmod b$. Then the algorithm is formulated in an extremely simple way:

$$\gcd(a, b) = \begin{cases}a,&\text{if }b = 0 \\ \gcd(b, a \bmod b),&\text{otherwise.}\end{cases}$$

## Implementation

```py
def gcd(a, b):
    if b == 0: return a

    return gcd(b, a % b)
```

## Time Complexity

The running time of the algorithm is estimated by Lamé's theorem, which establishes a surprising connection between the Euclidean algorithm and the Fibonacci sequence:

If $a > b \geq 1$ and $b < F_n$ for some $n$, the Euclidean algorithm performs at most $n-2$ recursive calls.

Moreover, it is possible to show that the upper bound of this theorem is optimal. When $a = F_n$ and $b = F_{n-1}$, $gcd(a, b)$ will perform exactly $n-2$ recursive calls. In other words, consecutive Fibonacci numbers are the worst case input for Euclid's algorithm.

Given that Fibonacci numbers grow exponentially, we get that the Euclidean algorithm works in $O(\log \min(a, b))$.

Another way to estimate the complexity is to notice that $a \bmod b$ for the case $a \geq b$ is at least $2$ times smaller than $a$, so the larger number is reduced at least in half on each iteration of the algorithm.

## Least common multiple

Calculating the least common multiple (commonly denoted **LCM**) can be reduced to calculating the GCD with the following simple formula:

$$\text{lcm}(a, b) = \frac{a \cdot b}{\gcd(a, b)}$$

Thus, LCM can be calculated using the Euclidean algorithm with the same time complexity:

A possible implementation, that cleverly avoids integer overflows by first dividing $a$ with the GCD, is given here:

```py
def lcm(a, b):
    return a // gcd(a, b) * b
```

## Resources

1. [Euclidean Algorithm - CP Algorithms](https://cp-algorithms.com/algebra/euclid-algorithm.html)

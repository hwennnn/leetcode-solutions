---
title: Sieve of Eratosthenes
tags:
  - algorithms
  - math
  - prime-numbers
date: 2023-10-22
---

## Introduction

The **Sieve of Eratosthenes** is a classic and efficient algorithm for finding all prime numbers up to a specified limit or for testing the primality of a specific number. This algorithm works by iteratively marking the multiples of each prime number, starting from 2, as composite (non-prime), gradually sieving out the non-prime numbers to reveal the prime numbers.

The idea behind is this: A number is prime, if none of the smaller prime numbers divides it. Since we iterate over the prime numbers in order, we already marked all numbers, who are divisible by at least one of the prime numbers, as divisible. Hence if we reach a cell and it is not marked, then it isn't divisible by any smaller prime number and therefore has to be prime.

## Implementation

```py
def generate_primes(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False

    for i in range(2, n + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False

    return isPrime
```

## Complexity

- Time complexity: $O(n \log \log n)$
- Space complexity: $O(n)$

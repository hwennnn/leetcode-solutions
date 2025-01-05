---
title: Digit DP
tags:
  - algorithms
  - dynamic-programming
date: 2023-10-21
---

## Introduction

**Digit DP** is a technique used to solve problems that asks you to find the number of integers within a range that satisfies some property based on the digits of the integers.

Typically, the ranges are between large integers (such as between $1$ and $10^{18}$), so looping through each integer and checking if it satisfies the given property is too slow.

Digit DP uses the digits of the integers to quickly count the number of integers with the given property in the range of integers.

## Implementation

Below is the example to count the total number of digit **1** appearing in all integers from the range of low to high.

The DP state will be `dp(index, tight, count)`.

```py
class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        N = len(s)
        digits = list(map(int, s))

        @cache
        def dp(index, tight, count):
            if index == N:
                return count

            limit = digits[index] if tight else 9
            res = 0

            for digit in range(limit + 1):
                res += dp(index + 1, tight and digit == digits[index], count + 1 if digit == 1 else count)

            return res

        return dp(0, True, 0)
```

> [!note]
> Depends on the problems, sometimes the variables such as **isLeading**, **isZero** will need to be included in the DP state.

### More examples

#### [Count the Number of Powerful Integers](https://leetcode.com/problems/count-the-number-of-powerful-integers/)

```py
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, maxDigits: int, s: str) -> int:
        s = list(map(int, s))

        def f(num):
            digits = list(map(int, str(num)))
            N = len(digits)

            @cache
            def dp(index, tight, suffixIndex):
                if index == N: return int(suffixIndex == len(s))

                limit = min(digits[index], maxDigits) if tight else maxDigits
                res = 0

                for digit in range(limit + 1):
                    nxtTight = tight and digits[index] == digit

                    if index + len(s) < N:
                        res += dp(index + 1, nxtTight, 0)
                    else:
                        if digit == s[suffixIndex]:
                            res += dp(index + 1, nxtTight, suffixIndex + 1)

                return res

            return dp(0, True, 0)

        return f(finish) - f(start - 1)
```

#### [Count number of unique digits](https://leetcode.com/problems/count-numbers-with-unique-digits/description)

```py
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -%3E int:
        if n == 0: return 1

        n = (10 ** n) - 1
        digits = []

        while n > 0:
            digits.append(n % 10)
            n //= 10

        digits.reverse()
        N = len(digits)

        @cache
        def dp(pos, tight, mask):
            if pos == N:
                return 1

            limit = digits[pos] if tight else 9
            res = 0

            for i in range(0, limit + 1):
                if mask & (1 << i) > 0: continue

                nextTight = tight and i == digits[pos]
                nextMask = mask if i == 0 and mask == 0 else mask ^ (1 << i)

                res += dp(pos + 1, nextTight, nextMask)

            return res

        return dp(0, True, 0)
```

## Complexity

- Time complexity: $O(10 * index * tight * count)$
- Space complexity: $O(d * tight * count)$, where d is the maximum number of digits given

## Resources

1. [Digit DP - GeeksforGeeks](https://www.geeksforgeeks.org/digit-dp-introduction/)
2. [Digit DP - Scaler](https://www.scaler.com/topics/data-structures/digit-dp/)
3. [Digit DP - Codeforces](https://codeforces.com/blog/entry/53960)
4. [Digit DP Problems List - LeetCode](https://leetcode.com/list/e62bv4a1)

---
title: Rabin-Karp Algorithm
tags:
  - algorithms
  - string
  - hashing
date: 2024-01-14
---

## Introduction

The **Rabin-Karp algorithm** is a string-matching algorithm that uses hashing to find an exact match of a pattern string in a text. Instead of checking character by character, it uses a rolling hash function to compare hash values of the pattern with hash values of substrings in the text. This makes it particularly efficient for multiple pattern matching.

The key features of Rabin-Karp are:

- Uses rolling hash function for $O(1)$ hash updates
- Handles multiple pattern matching efficiently
- Average case time complexity of $O(n + m)$
- Particularly useful in plagiarism detection and similar string matching problems

The main idea is to calculate hash values for the pattern and all possible substrings of the text of the same length as the pattern, then compare these hash values instead of comparing the strings directly.

## Implementation

### Python

```py
def rabin_karp(s, t):
    p = 31
    m = 10 ** 9 + 9
    S, T = len(s), len(t)

    p_pow = [0] * max(S, T)
    p_pow[0] = 1
    for i in range(1, len(p_pow)):
        p_pow[i] = (p_pow[i - 1] * p) % m

    h = [0] * (T + 1)
    for i in range(T):
        h[i + 1] = (h[i] + (ord(t[i]) - ord('a') + 1) * p_pow[i]) % m

    h_s = 0
    for i in range(S):
        h_s = (h_s + (ord(s[i]) - ord('a') + 1) * p_pow[i]) % m

    occurences = []
    for i in range(T - S + 1):
        cur_h = (h[i + S] + m - h[i]) % m
        if cur_h == h_s * p_pow[i] % m:
            occurences.append(i)

    return occurences
```

### C++

```cpp
vector<int> rabin_karp(string const& s, string const& t) {
    const int p = 31;
    const int m = 1e9 + 9;
    int S = s.size(), T = t.size();

    vector<long long> p_pow(max(S, T));
    p_pow[0] = 1;
    for (int i = 1; i < (int)p_pow.size(); i++)
        p_pow[i] = (p_pow[i-1] * p) % m;

    vector<long long> h(T + 1, 0);
    for (int i = 0; i < T; i++)
        h[i+1] = (h[i] + (t[i] - 'a' + 1) * p_pow[i]) % m;
    long long h_s = 0;
    for (int i = 0; i < S; i++)
        h_s = (h_s + (s[i] - 'a' + 1) * p_pow[i]) % m;

    vector<int> occurrences;
    for (int i = 0; i + S - 1 < T; i++) {
        long long cur_h = (h[i+S] + m - h[i]) % m;
        if (cur_h == h_s * p_pow[i] % m)
            occurrences.push_back(i);
    }
    return occurrences;
}
```

## Complexity

- Time complexity: $O(|T| + |S|)$ where $|T|$ is the length of text and $|S|$ is the length of pattern
  - Computing powers of p: $O(max(|T|, |S|))$
  - Computing hash values: $O(|T| + |S|)$
  - Finding occurrences: $O(|T| - |S| + 1)$
- Space complexity: $O(max(|T|, |S|))$
  - Powers array: $O(max(|T|, |S|))$
  - Hash values array: $O(|T|)$

## Resources

1. [Rabin-Karp Algorithm for string matching - CP Algorithm](https://cp-algorithms.com/string/rabin-karp.html)

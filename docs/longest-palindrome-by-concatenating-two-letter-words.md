---
id: longest-palindrome-by-concatenating-two-letter-words
title: Longest Palindrome by Concatenating Two Letter Words
description: Problem Description and Solution for Longest Palindrome by Concatenating Two Letter Words
sidebar_label: 2131. Longest Palindrome by Concatenating Two Letter Words
sidebar_position: 2131
---

# [2131. Longest Palindrome by Concatenating Two Letter Words](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/)

```py title=longest-palindrome-by-concatenating-two-letter-words.py
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        middle = 0
        res = 0
        counter = Counter()

        for word in words:
            if word[0] == word[1]:
                if counter[word] > 0:
                    counter[word] -= 1
                    res += 4
                    middle -= 1
                else:
                    middle += 1
                    counter[word] += 1
            else:
                if counter[word[::-1]] > 0:
                    counter[word[::-1]] -= 1
                    res += 4
                else:
                    counter[word] += 1
        
        if middle > 0:
            res += 2
        
        return res
```



---
id: minimum-number-of-moves-to-make-palindrome
title: Minimum Number of Moves to Make Palindrome
description: Problem Description and Solution for Minimum Number of Moves to Make Palindrome
sidebar_label: 2193. Minimum Number of Moves to Make Palindrome
sidebar_position: 2193
---

# [2193. Minimum Number of Moves to Make Palindrome](https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/)

```py title=minimum-number-of-moves-to-make-palindrome.py
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        n = len(s)
        s = list(s)
        start, end = 0, n - 1
        res = 0
        
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                i = end - 1
                
                while i > start and s[start] != s[i]:
                    i -= 1
                
                if start == i:
                    s[start], s[start + 1] = s[start + 1], s[start]
                    res += 1
                else:
                    while i < end:
                        s[i], s[i + 1] = s[i + 1], s[i]
                        i += 1
                        res += 1
                    
                    start += 1
                    end -= 1
        
        return res
```

```cpp title=minimum-number-of-moves-to-make-palindrome.cpp
// https://molchevskyi.medium.com/best-solutions-for-microsoft-interview-tasks-min-swaps-to-make-palindrome-e931689f8cae

class Solution {
public:
    int minMovesToMakePalindrome(string s) {
        int s_size = s.size();
        int result = 0;
        int start = 0, end = s_size - 1;

        while (end > start) {
            // if we found different chars
            if (s[start] != s[end]) {
                int i = end - 1; // make an additional iterator from the end

                // move toward the start until we found the same char
                while (i > start && s[i] != s[start]) { --i; }

                // if we scanned whole the string and found
                // no one the same char swap char on the 
                // start with adjacent char it needs for 
                // case when the first char is not on it's 
                // right place all other parts of the 
                // algorithm don't process a char on the start
                if (i == start) {
                    swap(s[start], s[start + 1]);
                    ++result;
                }
                // if the same character found swap all 
                // chars from i to the end
                else {
                    while (i < end) {
                        swap(s[i], s[i + 1]);
                        ++result;
                        ++i;
                    }
                    ++start; --end;
                }
            }
            // if s[start] == s[end] shrink the processing window
            else {
                ++start; --end;
            }
        }
        return result;
    }
};
```



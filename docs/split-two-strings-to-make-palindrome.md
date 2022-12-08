---
id: split-two-strings-to-make-palindrome
title: Split Two Strings to Make Palindrome
description: Problem Description and Solution for Split Two Strings to Make Palindrome
sidebar_label: 1616. Split Two Strings to Make Palindrome
sidebar_position: 1616
---

# [1616. Split Two Strings to Make Palindrome](https://leetcode.com/problems/split-two-strings-to-make-palindrome/)

```py title=split-two-strings-to-make-palindrome.py
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
        def isPalindrome(s, i, j):
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            
            return i >= j
        
        def check(a, b):
            i, j = 0, len(a) - 1
            while i < j and a[i] == b[j]:
                i += 1
                j -= 1
            
            return isPalindrome(a,i,j) or isPalindrome(b,i,j)
        
        return check(a,b) or check(b,a)
            
```

```cpp title=split-two-strings-to-make-palindrome.cpp
class Solution {
public:
    bool isPalindrome(string &s, int i, int j){
        while (i < j && s[i] == s[j])
            ++i, --j;
        return i >= j;
    }
    
    bool check(string &a, string &b){
        int i = 0, j = a.size() - 1;
        while (i < j && a[i] == b[j])
            ++i, --j;
        return isPalindrome(a, i, j) || isPalindrome(b, i, j);
    }
    
    bool checkPalindromeFormation(string a, string b) {
        return check(a,b) || check(b,a);   
    }
};
```



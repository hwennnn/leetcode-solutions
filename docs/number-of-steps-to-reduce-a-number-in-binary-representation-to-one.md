---
id: number-of-steps-to-reduce-a-number-in-binary-representation-to-one
title: Number of Steps to Reduce a Number in Binary Representation to One
description: Problem Description and Solution for Number of Steps to Reduce a Number in Binary Representation to One
sidebar_label: 1404. Number of Steps to Reduce a Number in Binary Representation to One
sidebar_position: 1404
---

# [1404. Number of Steps to Reduce a Number in Binary Representation to One](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/)

```py title=number-of-steps-to-reduce-a-number-in-binary-representation-to-one.py
class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s,2)
        res = 0
        while n > 1:
            if n & 1:
                n = -(~n)
            else:
                n >>= 1
        
            res += 1
        
        return res
```

```cpp title=number-of-steps-to-reduce-a-number-in-binary-representation-to-one.cpp
class Solution { // my own simulation 
public:
    int numSteps(string s) {        
        int ans = 0;
        while(s!="1"){
            const int n = s.size();
            if(s[n-1]=='0'){       // using right shift to simulate divide in binary          
               // s=s.substr(0,n-1); //ok
                s.pop_back(); // better
            }else{                 // binary addition
                int i = n - 1;
                for(; i>=0 && s[i]!='0'; i--) s[i]='0';
                if(i>= 0) s[i]='1';
                else 
                    s = '1'+s;
                    //s.insert(s.begin(), '1'); //ok
                    //s.insert(0, 1,'1'); //ok
            }
            ans++;
        }
        return ans;
    }
}; 
```



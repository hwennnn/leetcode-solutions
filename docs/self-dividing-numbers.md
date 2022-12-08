---
id: self-dividing-numbers
title: Self Dividing Numbers
description: Problem Description and Solution for Self Dividing Numbers
sidebar_label: 728. Self Dividing Numbers
sidebar_position: 728
---

# [728. Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/)

```py title=self-dividing-numbers.py
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        temp = []
        check = True
        for i in range(left,right+1):
            
            if i <10:
                temp.append(i)
            
            elif "0" not in str(i):

                for d in str(i):
                    if i%int(d) !=0:
                        print(i)
                        check = False
                        break
                if check:
                    temp.append(i)
        
            check = True
        return temp
```



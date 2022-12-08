---
id: largest-values-from-labels
title: Largest Values From Labels
description: Problem Description and Solution for Largest Values From Labels
sidebar_label: 1090. Largest Values From Labels
sidebar_position: 1090
---

# [1090. Largest Values From Labels](https://leetcode.com/problems/largest-values-from-labels/)

```py title=largest-values-from-labels.py
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        labels = [i[1] for i in sorted(enumerate(labels), key = lambda x:(-values[x[0]]))]
        values.sort(reverse = True)
        used = collections.defaultdict(int)
        
        res = i = 0
        
        while i < len(values) and num_wanted > 0:
            v, l = values[i], labels[i]
            
            if used[l] < use_limit:
                res += v
                used[l] += 1
                num_wanted -= 1
                
            i += 1
        
        return res
        
        
```



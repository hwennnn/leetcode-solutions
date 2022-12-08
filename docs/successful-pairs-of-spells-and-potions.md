---
id: successful-pairs-of-spells-and-potions
title: Successful Pairs of Spells and Potions
description: Problem Description and Solution for Successful Pairs of Spells and Potions
sidebar_label: 2300. Successful Pairs of Spells and Potions
sidebar_position: 2300
---

# [2300. Successful Pairs of Spells and Potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)

```py title=successful-pairs-of-spells-and-potions.py
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        res = []
        potions.sort()
        
        for spell in spells:
            index = bisect_left(potions, (success + spell - 1) // spell)
            res.append(n - index)
        
        return res
        
        
```



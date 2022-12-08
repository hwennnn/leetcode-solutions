---
id: check-if-there-is-a-valid-parentheses-string-path
title:  Check if There Is a Valid Parentheses String Path
description: Problem Description and Solution for  Check if There Is a Valid Parentheses String Path
sidebar_label: 2267.  Check if There Is a Valid Parentheses String Path
sidebar_position: 2267
---

# [2267.  Check if There Is a Valid Parentheses String Path](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/)

```py title=check-if-there-is-a-valid-parentheses-string-path.py
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        if grid[0][0] == ")": return False
        
        rows, cols = len(grid), len(grid[0])
        
        @cache
        def go(x, y, opened):
            if x == rows - 1 and y == cols - 1:
                return opened == 0
            
            def pos(dx, dy):
                if 0 <= dx < rows and 0 <= dy < cols:
                    if grid[dx][dy] == ")":
                        if opened >= 1:
                            return go(dx, dy, opened - 1)
                    else:
                        return go(dx, dy, opened + 1)
                        
                return False
            
            return pos(x + 1, y) or pos(x, y + 1)
        
        return go(0, 0, 1)
```



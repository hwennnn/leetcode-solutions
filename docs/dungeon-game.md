---
id: dungeon-game
title: Dungeon Game
description: Problem Description and Solution for Dungeon Game
sidebar_label: 174. Dungeon Game
sidebar_position: 174
---

# [174. Dungeon Game](https://leetcode.com/problems/dungeon-game/)

```py title=dungeon-game.py
class Solution:
    def calculateMinimumHP(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
        dp[rows][cols - 1] = dp[rows - 1][cols] = 1
        
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                need = min(dp[i][j + 1], dp[i + 1][j]) - mat[i][j]
                dp[i][j] = 1 if need <= 0 else need
        
        return dp[0][0]
```

```java title=dungeon-game.java
class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        if(dungeon == null || dungeon.length == 0 || dungeon[0].length == 0) return 1;
        
        int N = dungeon.length;
        int M = dungeon[0].length;
        int[][] dp = new int[N][M];
        dp[N - 1][M - 1] = 1 - dungeon[N - 1][M - 1];
        dp[N - 1][M - 1] = dp[N - 1][M - 1] <= 0 ? 1 : dp[N - 1][M - 1];
            
        for(int i = N - 1; i >= 0; --i){
            for(int j = M - 1; j >= 0; --j){
                if(i == N - 1 && j == M - 1) continue;
                int HP_D = i + 1 == N ? Integer.MAX_VALUE : dp[i + 1][j] - dungeon[i][j];
                int HP_R = j + 1 == M ? Integer.MAX_VALUE : dp[i][j + 1] - dungeon[i][j];
                int HP = Math.min(HP_D, HP_R);
                dp[i][j] = HP <= 0 ? 1 : HP;
            }    
        }
        
        return dp[0][0] ;
    }
}
```



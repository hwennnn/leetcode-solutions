---
id: find-the-winner-of-an-array-game
title: Find the Winner of an Array Game
description: Problem Description and Solution for Find the Winner of an Array Game
sidebar_label: 1535. Find the Winner of an Array Game
sidebar_position: 1535
---

# [1535. Find the Winner of an Array Game](https://leetcode.com/problems/find-the-winner-of-an-array-game/)

```cpp title=find-the-winner-of-an-array-game.cpp
class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        for (int i=1, j=0; i < arr.size() && j < k; ++i){
            if (arr[0] > arr[i])
                ++j;
            else{
                swap(arr[0], arr[i]);
                j = 1;
            }
                
        }
        
        return arr[0];
    }
};


```



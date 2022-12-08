---
id: prison-cells-after-n-days
title: Prison Cells After N Days
description: Problem Description and Solution for Prison Cells After N Days
sidebar_label: 957. Prison Cells After N Days
sidebar_position: 957
---

# [957. Prison Cells After N Days](https://leetcode.com/problems/prison-cells-after-n-days/)

```py title=prison-cells-after-n-days.py
class Solution:
    def prisonAfterNDays(self, cells: List[int], days: int) -> List[int]:
        
        def g(cells):
            masks = 0
            
            for cell, occupied in enumerate(cells):
                if occupied:
                    masks |= (1 << cell)
            
            return masks
        
        def transform(cells):
            new_cells = [0] * 8
            
            for i in range(1, 7):
                if cells[i - 1] == cells[i + 1]:
                    new_cells[i] = 1
            
            return new_cells
        
        original = cells[:]
        seen = set()
        cycle = 0
        hasCycle = False
        
        for _ in range(days):
            next_cells = transform(cells)
            masks = g(next_cells)
            
            if masks in seen:
                hasCycle = True
                break
            else:
                seen.add(masks)
                cycle += 1
            
            cells = next_cells
        
        if hasCycle:
            count = days % cycle
            
            for _ in range(count):
                cells = transform(cells)
            
        return cells
```

```java title=prison-cells-after-n-days.java
class Solution {
    public int[] prisonAfterNDays(int[] cells, int N) {
		if(cells==null || cells.length==0 || N<=0) return cells;
        boolean hasCycle = false;
        int cycle = 0;
        HashSet<String> set = new HashSet<>(); 
        for(int i=0;i<N;i++){
            int[] next = nextDay(cells);
            String key = Arrays.toString(next);
            if(!set.contains(key)){ //store cell state
                set.add(key);
                cycle++;
            }
            else{ //hit a cycle
                hasCycle = true;
                break;
            }
            cells = next;
        }
        if(hasCycle){
            N%=cycle;
            for(int i=0;i<N;i++){
                cells = nextDay(cells);
            }   
        }
        return cells;
    }
    
    private int[] nextDay(int[] cells){
        int[] tmp = new int[cells.length];
        for(int i=1;i<cells.length-1;i++){
            tmp[i]=cells[i-1]==cells[i+1]?1:0;
        }
        return tmp;
    }
}
```



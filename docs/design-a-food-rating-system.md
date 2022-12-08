---
id: design-a-food-rating-system
title: Design a Food Rating System
description: Problem Description and Solution for Design a Food Rating System
sidebar_label: 2353. Design a Food Rating System
sidebar_position: 2353
---

# [2353. Design a Food Rating System](https://leetcode.com/problems/design-a-food-rating-system/)

```py title=design-a-food-rating-system.py
from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.mp = {}
        self.A = defaultdict(SortedList)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.mp[food] = (cuisine, rating)
            self.A[cuisine].add((-rating, food))
        
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.mp[food]
        self.mp[food] = (cuisine, newRating)
        self.A[cuisine].remove((-rating, food))
        self.A[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.A[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
```



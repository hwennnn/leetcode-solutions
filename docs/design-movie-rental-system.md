---
id: design-movie-rental-system
title: Design Movie Rental System
description: Problem Description and Solution for Design Movie Rental System
sidebar_label: 1912. Design Movie Rental System
sidebar_position: 1912
---

# [1912. Design Movie Rental System](https://leetcode.com/problems/design-movie-rental-system/)

```py title=design-movie-rental-system.py
from sortedcontainers import SortedList

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.shops = collections.defaultdict(lambda: SortedList())
        self.rented = SortedList()
        self.movies = collections.defaultdict(lambda: collections.defaultdict(int))
        
        for shop,movie,price in entries:
            self.movies[shop][movie] = price
            self.shops[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        return [shop for _, shop in self.shops[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.movies[shop][movie]
        self.shops[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.movies[shop][movie]
        self.shops[movie].add((price, shop))
        self.rented.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for _,shop,movie in self.rented[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
```



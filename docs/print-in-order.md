---
id: print-in-order
title: Print in Order
description: Problem Description and Solution for Print in Order
sidebar_label: 1114. Print in Order
sidebar_position: 1114
---

# [1114. Print in Order](https://leetcode.com/problems/print-in-order/)

```py title=print-in-order.py
from threading import Condition

class Foo:
    def __init__(self):
        self.exec_condition = Condition()
        self.order = 0
        self.first_finish = lambda: self.order == 1
        self.second_finish = lambda: self.order == 2

    def first(self, printFirst):
        with self.exec_condition:
            printFirst()
            self.order = 1
            self.exec_condition.notify(2)

    def second(self, printSecond):
        with self.exec_condition:
            self.exec_condition.wait_for(self.first_finish)
            printSecond()
            self.order = 2
            self.exec_condition.notify()

    def third(self, printThird):
        with self.exec_condition:
            self.exec_condition.wait_for(self.second_finish)
            printThird()
```



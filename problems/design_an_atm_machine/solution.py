class ATM:

    def __init__(self):
        self.curr = [0] * 5
        self.notes = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, x in enumerate(banknotesCount):
            self.curr[i] += x

    def withdraw(self, amount: int) -> List[int]:
        used = [0] * 5
        
        for i in range(4, -1, -1):
            if self.notes[i] > amount:
                continue
            
            can = min(self.curr[i], amount // self.notes[i])
            used[i] += can
            amount -= can * self.notes[i]
        
        if amount != 0:
            return [-1]
        
        for i, x in enumerate(used):
            self.curr[i] -= x
        
        return used
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.count = 0
        self.discount = discount
        self.products = products
        self.prices = prices

    def getBill(self, P: List[int], A: List[int]) -> float:
        self.count += 1
        price = 0
        for p,a in zip(P,A):
            price += self.prices[self.products.index(p)] * a

        if self.count%self.n == 0:
            price -= (price * (self.discount/100))
            
        return price


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
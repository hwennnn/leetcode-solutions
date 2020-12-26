class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lst = [big,medium,small]

    def addCar(self, carType: int) -> bool:
        t = carType - 1
        if self.lst[t] > 0:
            self.lst[t] -= 1
            return True
        
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
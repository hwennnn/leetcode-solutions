class Robot:

    def __init__(self, width: int, height: int):
        self.rows = width
        self.cols = height
        self.x = 0
        self.y = 0
        self.di = 0
        self.words = ["East", "North", "West", "South"]
        self.cycle = (width + height - 2) * 2
    
    def getNextSteps(self, x, y):
        if self.di == 0:
            return (x + 1, y)
        elif self.di == 1:
            return (x, y + 1)
        elif self.di == 2:
            return (x - 1, y)
        else:
            return (x, y - 1)

    def move(self, num: int) -> None:
        num %= self.cycle
        
        if num == 0:
            if self.x == 0 and self.y == 0:
                self.di = 3
            elif self.x == self.rows - 1 and self.y == 0:
                self.di = 0
            elif self.x == self.rows - 1 and self.y == self.cols - 1:
                self.di = 1
            elif self.x == 0 and self.y == self.cols - 1:
                self.di = 2
            
        for _ in range(num):
            dx, dy = self.getNextSteps(self.x, self.y)
            if not (0 <= dx < self.rows and 0 <= dy < self.cols):
                self.di = (self.di + 1) % 4
                dx, dy = self.getNextSteps(self.x, self.y)
            self.x, self.y = dx, dy

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.words[self.di]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
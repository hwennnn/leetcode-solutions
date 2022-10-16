class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        for x in text:
            self.left.append(x)

    def deleteText(self, k: int) -> int:
        res = 0
        
        while self.left and k > 0:
            res += 1
            self.left.pop()
            k -= 1
        
        return res
            
    def cursorLeft(self, k: int) -> str:
        while self.left and k > 0:
            self.right.append(self.left.pop())
            k -= 1
        
        return "".join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        while self.right and k > 0:
            self.left.append(self.right.pop())
            k -= 1
        
        return "".join(self.left[-10:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
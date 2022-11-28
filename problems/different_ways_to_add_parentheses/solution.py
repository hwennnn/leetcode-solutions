class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        N = len(expression)
        res = []

        for i, x in enumerate(expression):
            if x in "+-*":
                first = expression[:i]
                second = expression[i + 1:]

                firstPart = self.diffWaysToCompute(first)
                secondPart = self.diffWaysToCompute(second)

                for a in firstPart:
                    for b in secondPart:
                        if x == "+":
                            res.append(a + b)
                        elif x == "-":
                            res.append(a - b)
                        elif x == "*":
                            res.append(a * b)
                        
        if len(res) == 0:
            res.append(int(expression))

        return res
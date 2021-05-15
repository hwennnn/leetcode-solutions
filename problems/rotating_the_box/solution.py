class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        box = [[box[j][i] for j in range(rows)][::-1] for i in range(cols-1,-1,-1)][::-1]
        rows, cols = cols, rows
        
        for j in range(cols):
            canDrop = False
            available = deque()
            prior = deque()
            for i in reversed(range(rows)):
                if box[i][j] == ".":
                    canDrop = True
                elif box[i][j] == "*":
                    canDrop = False
                    available.clear()
                    prior.clear()
                
                if canDrop:
                    if box[i][j] == ".":
                        available.append(i)
                
                    elif box[i][j] == "#":
                        if available or prior:
                            if available and prior:
                                ii = available.popleft() if available[0] > prior[0] else prior.popleft()
                            else:
                                ii = available.popleft() if available else prior.popleft()
                                    
                            box[ii][j] = '#'
                            box[i][j] = '.'
                            prior.append(i)
        
        return box
        
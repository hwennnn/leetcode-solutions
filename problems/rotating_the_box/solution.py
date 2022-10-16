class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        
        for row in box:
            pos = cols - 1
            for j in range(cols - 1, -1, -1):
                if row[j] == '*':
                    pos = j - 1
                elif row[j] == '#':
                    row[j], row[pos] = row[pos], row[j]
                    pos -= 1
        
        return zip(*box[::-1])
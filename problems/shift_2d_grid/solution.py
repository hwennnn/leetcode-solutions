class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        
        m = len(grid)
        n = len(grid[0])

        temp = [x for i in grid for x in i]

        shift = k%len(temp)

        lst = temp[len(temp)-shift:] + temp[:len(temp)-shift]

        ans = []
        count = 0
        for row in range(m):
            x = []

            for column in range(n):
                x.append(lst[count])
                count+=1

            ans.append(x)   

        return ans
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        queue = collections.deque()
        
        for x in range(rows):
            for y in [0, cols - 1]:
                if board[x][y] == 'O':
                    board[x][y] = 'G'
                    queue.append((x, y))
        
        for x in [0, rows - 1]:
            for y in range(cols):
                if board[x][y] == 'O':
                    board[x][y] = 'G'
                    queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and board[dx][dy] == 'O':
                    board[dx][dy] = 'G'
                    queue.append((dx, dy))
        
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'G':
                    board[x][y] = 'O'
            
        
        
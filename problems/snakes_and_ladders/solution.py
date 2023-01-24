class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        G = {}

        def f(v):
            row = N - 1 - (v - 1) // N
            col = (v - 1) % N
            if (v - 1) // N % 2:
                col = N - 1 - col

            return (row, col)
        
        dq = deque([1])
        seen = {1}
        moves = 1

        while dq:
            for _ in range(len(dq)):
                index = dq.popleft()

                for adj in range(index + 1, min(index + 6, N * N) + 1):
                    r, c = f(adj)
                    
                    if board[r][c] != -1:
                        adj = board[r][c]
                    
                    if adj == N * N: return moves

                    if adj not in seen:
                        seen.add(adj)
                        dq.append(adj)
            
            moves += 1

        return -1
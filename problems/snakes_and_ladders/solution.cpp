class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = (int)board.size();
        int m = n * n;
        
        vector<bool> visited(m + 1, false);
        visited[1] = true;
        deque<int> queue = {1};
        int moves = 1;
        
        while (!queue.empty()) {
            for (int i = 0, l = (int)queue.size(); i < l; i++) {
                int u = queue.front();
                queue.pop_front();
                for (int v = u + 1, k = min(m, u + 6); v <= k; v++) {
                    int y = n - 1 - (v - 1) / n;
                    int x = (v - 1) % n;
                    if ((v - 1) / n % 2) x = n - 1 - x;
                    int w = board[y][x] == -1 ? v : board[y][x];
                    if (w == m) return moves;
                    if (!visited[w]) {
                        visited[w] = true;
                        queue.push_back(w);
                    }
                }
            }
            moves++;
        }
        
        return -1;
    }
};
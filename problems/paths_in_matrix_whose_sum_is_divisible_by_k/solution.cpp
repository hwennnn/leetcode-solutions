class Solution {
public:
    const long long M = 1e9 + 7;
    
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        int rows = grid.size(), cols = grid[0].size();
        long long cache[rows][cols][k];
        memset(cache, -1, sizeof(cache));
        
        function<long long(int, int, int)> go = [&](int i, int j, int curr) {
            if (cache[i][j][curr] != -1) return cache[i][j][curr];
            
            if (i == rows - 1 && j == cols - 1) return (long long)(curr == 0);

            long long count = 0;

            if (i + 1 < rows) {
                count += go(i + 1, j, (curr + grid[i + 1][j]) % k);
                count %= M;
            }

            if (j + 1 < cols) {
                count += go(i, j + 1, (curr + grid[i][j + 1]) % k);
                count %= M;
            }

            return cache[i][j][curr] = count;
        };
        
        return go(0, 0, grid[0][0] % k);
    }
};
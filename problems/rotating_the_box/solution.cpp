// OJ: https://leetcode.com/contest/biweekly-contest-52/problems/rotating-the-box/
// Author: github.com/lzl124631x
// Time: O(MN)
// Space: O(1)
class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& A) {
        int M = A.size(), N = A[0].size();
        vector<vector<char>> ans(N, vector<char>(M, '.'));
        for (int i = 0; i < M; ++i) {
            int w = N - 1; // `w` is the write pointer
            for (int j = N - 1; j >= 0; --j) {
                if (A[i][j] == '.') continue;
                if (A[i][j] == '#') {
                    ans[w--][M - i - 1] = '#'; // write stone to position `(w, M - i - 1)` and move write pointer
                } else {
                    ans[j][M - i - 1] = '*';
                    w = j - 1; // move the writer pointer to the position after the obstacle
                }
            }
        }
        return ans;
    }
};
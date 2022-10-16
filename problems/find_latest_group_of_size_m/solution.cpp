class Solution {
public:
     int findLatestStep(vector<int>& A, int m) {
        int res = -1, n = A.size();
        vector<int> length(n + 2), count(n + 1);
        for (int i = 0; i < n; ++i) {
            int a = A[i], left = length[a - 1], right = length[a + 1];
            length[a] = length[a - left] = length[a + right] = left + right + 1;
            count[left]--;
            count[right]--;
            count[length[a]]++;
            if (count[m])
                res = i + 1;
        }
        return res;
    }
};
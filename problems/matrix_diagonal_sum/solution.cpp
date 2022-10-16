class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int res = 0;
        int N = mat.size();
        
        for (int i = 0, j = N-1; i < N; i++, j--){
            if (i == j){
                res += mat[i][i];
            }else{
                res += mat[i][j] + mat[i][i];
            }
        }
        
        return res;
    }
};
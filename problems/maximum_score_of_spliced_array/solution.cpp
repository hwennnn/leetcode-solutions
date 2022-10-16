// https://leetcode.com/discuss/interview-question/2189149/Amazon-Online-Assessment-Questions

class Solution {
public:
    vector<int> bestSplice(vector<int>& A, vector<int>& B) {
        // find the maximum subarray sum in B-A
        vector<int> ans(A.size());
        for (int i = 0; i < A.size(); i++) {
            ans[i] = B[i] - A[i];
        }

        int best = INT_MIN, start = 0, end = 0;
        int cur = 0, last = 0, cur_start = 0;
        for (int i = 0; i < ans.size(); i++) {
            if (last <= 0) cur_start = i;
            cur = ans[i] + max(last, 0);
            if (cur >= best) {
                best = cur;
                start = cur_start;
                end = i;
            }
            last = cur;
        }

        // copy over the ranges from A and B
        for (int i = 0; i < A.size(); i++) {
            ans[i] = A[i];
        }
        // only copy over the range from B if it increases the final sum
        if (best > 0) {
            for (int i = start; i <= end; i++) {
                ans[i] = B[i];
            }
        }
        return ans;
    }
    
    int maximumsSplicedArray(vector<int>& A, vector<int>& B) {
        vector<int> A_res = bestSplice(A, B);
        vector<int> B_res = bestSplice(B, A);

        // return the larger sum
        int A_sum = 0, B_sum = 0;
        for (int i = 0; i < A.size(); i++) {
            A_sum += A_res[i];
            B_sum += B_res[i];
        }

        return A_sum > B_sum ? A_sum : B_sum;
    }
};


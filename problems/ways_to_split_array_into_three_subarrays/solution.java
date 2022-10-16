class Solution {
    public int waysToSplit(int[] nums) {

        int MOD = (int) (1e9 + 7);

        int N = nums.length;

        // prefix array
        int[] A = new int[N];
        A[0] = nums[0];
        for (int i = 1; i < N; ++i) A[i] = A[i - 1] + nums[i];

        int res = 0;
        for (int i = 1; i < N - 1; ++i) {

            int left = helper(A, A[i - 1], i, true);
            int right = helper(A, A[i - 1], i, false);

            if (left == -1 || right == -1) continue;  // none is satisfied

            res = (res + (right - left + 1) % MOD) % MOD;
        }

        return res;
    }

    private int helper(int[] A, int leftSum, int index, boolean searchLeft) {

        int N = A.length;
        int l = index, r = N - 2;
        int res = -1;

        while (l <= r) {

            int m = (r - l) / 2 + l;

            int midSum = A[m] - A[index - 1];
            int rightSum = A[N - 1] - A[m];

            if (leftSum <= midSum && midSum <= rightSum) {
                res = m;
                if (searchLeft) r = m - 1;
                else l = m + 1;
            } else if (leftSum > midSum) {  // shrink left
                l = m + 1;
            } else {  // shrink right
                r = m - 1;
            }
        }

        return res;
    }
}
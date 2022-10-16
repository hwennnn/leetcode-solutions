class Solution {
    public int findLongestChain(int[][] pairs) {
        int n = pairs.length;
        if (pairs == null || n == 0) return 0;
        Arrays.sort(pairs, (a, b) -> (a[0] - b[0]));
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < i; j++){
                dp[i] = Math.max(dp[i], pairs[i][0] > pairs[j][1] ? dp[j] + 1 : dp[j]);
            }
        }
        
        
        return dp[n-1];
    }
}
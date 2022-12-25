class Solution {
public:
    int N, K;
    int MOD = 1e9 + 7;
    int cache[1001][1001];

    int powmod (int a, int b, int k) {
        int result = 1 ;
        while (b--) {
            result *= a ;
            result %= k ;
        }
        return result ;
    }

    int dp(vector<int>& nums, int index, int s) {
        if (cache[index][s] != -1) {
            return cache[index][s];
        }

        if (s >= K) return 0;
        if (index >= N) return 1;

        int skip = dp(nums, index + 1, s);
        int take = s + nums[index] <= 1000 ? dp(nums, index + 1, s + nums[index]) : 0;

        return cache[index][s] = (skip + take) % MOD;
    }

    int countPartitions(vector<int>& nums, int k) {
        long long total = accumulate(nums.begin(), nums.end(), 0LL);
        if (total < 2 * k) return 0;

        memset(cache, -1, sizeof(cache));
        N = nums.size();
        K = k;
        
        int all = powmod(2, N, MOD);
        int invalid = 2 * dp(nums, 0, 0);

        return (all - invalid + MOD) % MOD;
    }
};
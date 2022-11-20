class Solution {
public:
    const int M = 1e9 + 7;
    int cache[1001][1001];

    bool isPrime(char x) {
        return x == '2' || x == '3' || x == '5' || x == '7';
    }

    int go(int index, int parts, string& s, int k, int minLength, int N) {
        if (cache[index][parts] != -1) return cache[index][parts];
            
        if (parts >= k) return cache[index][parts] = 0;

        if (parts == k - 1) return cache[index][parts] = (N - index >= minLength);

        int res = 0;

        for (int j = index + minLength; j < N - (k - parts - 1) * minLength + 1; j++) {
            if (isPrime(s[j]) && !isPrime(s[j - 1])) {
                res += go(j, parts + 1, s, k, minLength, N);
                res %= M;
            }
        }

        return cache[index][parts] = res;
    }

    int beautifulPartitions(string s, int k, int minLength) {
        int N = s.size();
        memset(cache, -1, sizeof(cache));

        if (!isPrime(s[0]) || isPrime(s[N - 1])) return 0;
        
        return go(0, 0, s, k, minLength, N);
    }
};
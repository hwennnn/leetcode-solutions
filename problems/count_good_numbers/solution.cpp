class Solution {
public:
    int M = 1e9 + 7;
    
    long long power(long long base, long long exp){
        if (exp == 0) return 1;
        
        long long res = power(base, exp / 2) % M;
        
        res *= res;
        res %= M;
        
        if (exp & 1)
            res *= base;
        res %= M;
        
        return res;
    }
    int countGoodNumbers(long long n) {
        long long even = (n + 1) / 2;
        long long odd = n - even;
        
        return (power(5, even) * power(4, odd)) % M;
    }
};
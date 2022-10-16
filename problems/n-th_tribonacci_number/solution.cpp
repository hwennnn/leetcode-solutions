class Solution {
public:
    int arr[38];
    int recur(int n){
        if (arr[n] != -1) return arr[n];
        int result = recur(n-1) + recur(n-2) + recur(n-3);
        arr[n] = result;
        return result;
    }
    int tribonacci(int n) {
        fill_n(arr, 38, -1);
        arr[0] = 0;
        arr[1] = 1;
        arr[2] = 1;
        return recur(n);
    }
};
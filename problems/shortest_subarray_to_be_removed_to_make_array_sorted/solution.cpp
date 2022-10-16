class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int n = arr.size();
        int left = 0;
        while (left+1 < n && arr[left+1] >= arr[left]) left++;
        if (left+1 == n) return 0;

        int right = n-1;
        while (right > left && arr[right-1] <= arr[right]) right--;

        int res = min(n - left - 1, right);
        int i = 0, j = right;

        while (i <= left && j < n){
            if (arr[j] >= arr[i]){
                res = min(res, j - i - 1);
                i++;
            }else{
                j++;
            }
        }

        return res;
    }
};
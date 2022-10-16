class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        for (int i=1, j=0; i < arr.size() && j < k; ++i){
            if (arr[0] > arr[i])
                ++j;
            else{
                swap(arr[0], arr[i]);
                j = 1;
            }
                
        }
        
        return arr[0];
    }
};


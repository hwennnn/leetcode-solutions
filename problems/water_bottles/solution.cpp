class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int res = numBottles;
        
        while (numBottles >= numExchange){
            int remaining = numBottles % numExchange;
            numBottles /= numExchange;
            res += numBottles;
            numBottles += remaining;
        }
           
        return res;
        
    }
};
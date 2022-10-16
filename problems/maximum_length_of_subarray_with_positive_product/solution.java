class Solution {
      public int getMaxLen(int[] nums) {
        // sum is used to count the number of negative numbers from zeroPosition to current index
        int firstNegative = -1, zeroPosition = -1, sum = 0, max = 0;
        for(int i = 0;i < nums.length; i++){
            if(nums[i] < 0){
                sum++;
				// we only need to know index of first negative number
                if(firstNegative == -1) firstNegative = i;
            }
			// if current number is 0, we can't use any element from index 0 to i anymore, so update zeroPosition, and reset sum and firstNegative. If it is a game, we should refresh the game when we meet 0. 
            if(nums[i] == 0){
                sum = 0;
                firstNegative = -1;
                zeroPosition = i;
            }
            else{
			    // consider index of zero
                if(sum%2 == 0) max = Math.max(i - zeroPosition, max);
				// consider index of first negative number
                else max = Math.max(i - firstNegative, max);   
            }
        }
        return max;
    }
}
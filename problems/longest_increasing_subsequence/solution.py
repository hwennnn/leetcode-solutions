class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        st = []
        
        for x in nums:
            index = bisect.bisect_left(st, x)
            if index < len(st):
                st[index] = x
            else:
                st.append(x)
        
        return len(st)
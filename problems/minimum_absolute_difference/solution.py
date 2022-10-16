class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        mp = collections.defaultdict(list)
        arr.sort()
        mmin = float('inf')
        n = len(arr)
        
        for i in range(1, n):
            diff = arr[i] - arr[i - 1]
            mmin = min(mmin, diff)
            mp[diff].append([arr[i - 1], arr[i]])
        
        return mp[mmin]
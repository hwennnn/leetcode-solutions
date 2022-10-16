class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        for perm in permutations(sorted(arr, reverse = 1)):
            if perm[0] * 10 + perm[1] < 24 and perm[2] < 6:
                return f"{perm[0]}{perm[1]}:{perm[2]}{perm[3]}"
        
        return ""
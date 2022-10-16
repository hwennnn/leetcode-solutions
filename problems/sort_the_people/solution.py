class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        A = sorted([(a, b) for a, b in zip(names, heights)], key = lambda x : (-x[1]))
        
        return [a for a, _ in A]
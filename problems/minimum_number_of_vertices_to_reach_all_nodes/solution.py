class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        nums = set()
        not_edge = set()
        res = []
        
        for edge in edges:
            if edge[0] not in nums:
                nums.add(edge[0])
            if edge[1] not in nums:
                nums.add(edge[1])
            if edge[1] not in not_edge:
                not_edge.add(edge[1])
        

        for num in nums:
            if num not in not_edge:
                res.append(num)
        return res
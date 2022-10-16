class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        level = nodes = 1
        
        while label >= nodes * 2:
            nodes *= 2
            level += 1
        
        while label != 0:
            res.append(label)
            mmax = (2 ** level) - 1
            mmin = 2 ** (level - 1)
            label = (mmax + mmin - label) // 2
            level -= 1
        
        return res[::-1]
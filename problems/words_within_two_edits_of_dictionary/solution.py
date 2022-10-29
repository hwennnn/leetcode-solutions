class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        
        for query in queries:
            for dictWord in dictionary:
                diff = sum(1 for a, b in zip(query, dictWord) if a != b)

                if diff <= 2:
                    res.append(query)
                    break

        return res
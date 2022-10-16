class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        dic = {rounds[0]:1}
        N = len(rounds)
        for i in range(N-1):
            this_round = rounds[i]
            next_round = rounds[i+1]

            while this_round != next_round:
                if this_round < n:
                    this_round += 1
                else:
                    this_round = 1

                if this_round not in dic:
                    dic[this_round] = 1
                else:
                    dic[this_round] += 1

        m = max(dic.values())
        res = []
        for key in dic:
            if dic[key] == m:
                res.append(key)
        res.sort()
        return res
            

            
            
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        res = [-1] * n
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def go(node, prev):
            k = ord(labels[node]) - ord('a')
            cnt = [0] * 26
            cnt[k] += 1

            for nei in graph[node]:
                if nei != prev:
                    child = go(nei, node)

                    for i in range(26):
                        cnt[i] += child[i]

            res[node] = cnt[k]

            return cnt

        go(0, -1)
        return res
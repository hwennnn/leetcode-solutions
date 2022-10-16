class Solution:
    def isEscapePossible(self, blocked, source, target):
        blocked = set(map(tuple, blocked))

        def dfs(x, y, target, seen):
            if not (0 <= x < 10**6 and 0 <= y < 10**6) or (x, y) in blocked or (x, y) in seen: return False
            
            seen.add((x, y))
            if len(seen) > 20000 or [x, y] == target: return True
            return dfs(x + 1, y, target, seen) or \
                dfs(x - 1, y, target, seen) or \
                dfs(x, y + 1, target, seen) or \
                dfs(x, y - 1, target, seen)
        
        return dfs(source[0], source[1], target, set()) and dfs(target[0], target[1], source, set())
        
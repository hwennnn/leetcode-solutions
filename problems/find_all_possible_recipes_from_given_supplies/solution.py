class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = []
        n = len(recipes)
        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        supplies = set(supplies)
        
        for i in range(n):
            for ing in ingredients[i]:
                if ing not in supplies:
                    indegree[recipes[i]] += 1
                    graph[ing].append(recipes[i])
        
        queue = collections.deque()
        
        for recipe in recipes:
            if indegree[recipe] == 0:
                queue.append(recipe)
        
        while queue:
            n = len(queue)
            
            for _ in range(n):
                recipe = queue.popleft()

                res.append(recipe)
                
                for nei in graph[recipe]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
        
        return res
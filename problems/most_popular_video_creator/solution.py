class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        viewCount = defaultdict(int)
        popularVideo = {}
        mostViews = 0
        
        for creator, uid, view in zip(creators, ids, views):
            viewCount[creator] += view
            mostViews = max(mostViews, viewCount[creator])
            
            if creator not in popularVideo:
                popularVideo[creator] = (view, uid)
            else:
                if view > popularVideo[creator][0] or (view == popularVideo[creator][0] and uid < popularVideo[creator][1]):
                    popularVideo[creator] = (view, uid)
        
        res = []
        for creator, totalViews in viewCount.items():
            if totalViews == mostViews:
                res.append((creator, popularVideo[creator][1]))
        
        return res
                    
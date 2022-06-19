class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        mp = defaultdict(list)
        products.sort()
        
        for product in products:
            curr = ""
            
            for x in product:
                curr += x
                if len(mp[curr]) == 3: continue
                mp[curr].append(product)
        
        res = []
        curr = ""
        for word in searchWord:
            curr += word
            res.append(mp[curr][:3])
        
        return res
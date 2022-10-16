class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        check = 0
        if ruleKey == "color": check = 1
        elif ruleKey == "name": check = 2
        
        res = 0
        for item in items:
            if item[check] == ruleValue:
                res += 1
        
        return res
        
        
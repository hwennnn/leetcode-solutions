class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        
        for log in logs:
            if log == "./":
                continue
            # if depth > 0:
            if depth > 0:
                if log == "../":
                    depth -= 1
                    continue
            
            if log != "../" and log != "./":
                depth += 1
        
        return depth
                
                
                
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let = []
        dig = []
        
        for index, log in enumerate(logs):
            space = log.index(" ")
            content = log[space + 1:]
            d = log[:space]
            
            if any(digit in content for digit in "1234567890"):
                dig.append(log)
            else:
                let.append((content, d, index))
        
        return [logs[index] for _, __, index in sorted(let)] + dig
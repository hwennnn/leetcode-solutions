class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        mp = defaultdict(int)
        
        for message, sender in zip(messages, senders):
            mp[sender] += len(message.split())

        currCount = float('-inf')
        res = ""

        for sender, count in mp.items():
            if count > currCount:
                currCount = count
                res = sender
            elif count == currCount:
                res = max(res, sender)
        
        return res
        
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.ktov = {}
        
        for k, v in zip(keys, values):
            self.ktov[k] = v
        
        self.count = Counter(self.encrypt(x) for x in dictionary)
        

    def encrypt(self, word1: str) -> str:
        res = []
        
        for x in word1:
            if x in self.ktov:
                res.append(self.ktov[x])
            else:
                return ""
        
        return "".join(res)

    def decrypt(self, word2: str) -> int:
        return self.count[word2]


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
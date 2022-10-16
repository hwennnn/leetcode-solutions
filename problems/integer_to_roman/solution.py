class Solution:
    def intToRoman(self, num):
        mp = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        
        for letter, n in zip(mp, nums):
            result += letter * (num // n)
            num %= n
            
        return result
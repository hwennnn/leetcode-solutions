class Solution:
    def champagneTower(self, p, qr, qg):
        res = [[0.0]*i for i in range(1, qr + 2)]
        res[0][0] = p
        
        for i in range(qr):
            for j in range(len(res[i])):
                if res[i][j] > 1:
                    res[i+1][j] += (res[i][j] - 1) / 2
                    res[i+1][j+1] += (res[i][j] - 1) / 2
                    res[i][j] = 1
        
        return res[qr][qg] if res[qr][qg] < 1 else 1
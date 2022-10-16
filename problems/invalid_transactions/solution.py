class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans = []
        length = len(transactions)
        if not length: return ans
        name,time,money,city = [],[],[],[]
        add = [1] * length
        
        for trans in transactions:
            tran = trans.split(',')
            name.append(tran[0])
            time.append(int(tran[1]))
            money.append(int(tran[2]))
            city.append(tran[3])
            
        for i in range(length):
            if money[i] > 1000:
                add[i] = False
            for j in range(i+1,length):
                if name[i] == name[j] and abs(time[i]-time[j])<= 60 and city[i]!=city[j]:
                    add[i] = False
                    add[j] = False
                    
        for ind,val in enumerate(add):
            if not val:
                ans.append(transactions[ind])
                
        return ans
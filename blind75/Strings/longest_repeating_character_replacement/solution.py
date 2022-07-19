#Its sliding window problem by amintaining two pointers and calaculating number of times the less frequently character occures. formula is len(substring) - less frequent char <= k.
class solution:
    def solve(self,s,k):
        tmp = {}
        max_value = 0
        i=0
        for j in range(len(s)):
            tmp[s[j]] = 1 + tmp.get(s[j],0)
            while j - i + 1 - max(tmp.values()) > k:
                tmp[s[i]] -= 1            
                i+=1    
            max_value = max(max_value, j-i+1)
        return max_value          
                       

   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve("AABABBA",1)
    print(result)
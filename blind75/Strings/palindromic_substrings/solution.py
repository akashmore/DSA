class solution:
    def solve(self,s):
        count = 0
        for i in range(0,len(s)):
            #odd length
            l,r = i, i
            while l  >= 0 and r < len(s) and s[l] == s[r]:
                  count+=1
                  l-=1
                  r+=1
            #even Length
            l,r = i,i+1
            while l  >= 0 and r < len(s) and s[l] == s[r]:
                  count+=1
                  l-=1
                  r+=1
        return count  
if __name__ == '__main__':
    obj = solution()
    result = obj.solve("aaa")
    print(result)
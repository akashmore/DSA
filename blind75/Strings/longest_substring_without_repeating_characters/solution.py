class solution:
    def solve(self,s):
        if s == " " or len(s) == 1:
            return 1 
        max_len = 0
        for i in range(0,len(s)):
            tmp = {}
            cnt = 0
            for j in range(i,len(s)):                
                if s[j] not in tmp:
                    tmp[s[j]] = True
                    cnt+=1
                else:
                    max_len = max(max_len,cnt)
                    break
            max_len = max(max_len,cnt)
        return max_len            
                       

   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve("au")
    print(result)

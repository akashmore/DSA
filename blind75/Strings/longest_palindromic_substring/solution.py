
#Bruteforce approach
# class solution:
#     def solve(self,s):
#         max_len = 0
#         max_str = "" 
#         for i in range(0,len(s)):
#             for j in range(i+1,len(s)):
#                 for k in range(i,j):
#                     if s[i:k+1] == s[i:k+1][::-1]:
#                         if len(s[i:k+1]) > max_len:
#                             max_len = max(max_len,len(s[i:k+1]))
#                             max_str = s[i:k+1]
#         return max_str

#start from middle and check if left string equals right string
class solution:
    def solve(self,s):
        max_len = 0
        max_str = ""
        for i in range(0,len(s)):
            #odd length
            l,r = i, i
            while l  >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r]) > max_len:
                    max_len = max(max_len,len(s[l:r]))
                    max_str = s[l:r+1]
                l-=1
                r+=1
            
            #even Length
            l,r = i,i+1
            while l  >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r]) > max_len:
                    max_len = max(max_len,len(s[l:r]))
                    max_str = s[l:r+1]
                l-=1
                r+=1
        return max_str
          
if __name__ == '__main__':
    obj = solution()
    result = obj.solve("cbbd")
    print(result)
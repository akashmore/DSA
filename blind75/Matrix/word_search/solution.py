#maintain 4 pointer top,bottom,left,right
class solution:
    def solve(self,matrix,word):
        rows,cols = len(matrix),len(matrix[0])
        visited_set = set()
       
        def dfs(r,c,i):
           if i == len(word):
               return True
           if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != matrix[r][c] or (r,c) in visited_set):
               return False
           visited_set.add((r,c))
           res = (dfs(r+1,c,i+1) or
                  dfs(r-1,c,i+1) or
                  dfs(r,c+1,i+1) or
                  dfs(r,c-1,i+1))
           visited_set.remove((r,c))
           return res
        for i in range(rows):
           for j in range(cols):
               if dfs(i,j,0):
                   return True
        return False
                
if __name__ == '__main__':
    obj = solution()
    result = obj.solve([["C","A","A"],
                        ["A","A","A"],
                        ["B","C","D"]],"AAB")
    print(result)
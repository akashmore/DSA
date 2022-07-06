import copy
class solution:
    #below is log(m.n) solution with extra dummy array
    def solve(self,matrix):
        copy_arr = copy.deepcopy(matrix)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == 0:
                    self.set_zeroes(i,j,copy_arr)
        return copy_arr
    
    def set_zeroes(self,i_index,j_index,copy_arr):
        for i in range(0,len(copy_arr)):
            for j in range(0,len(copy_arr[0])):
                if i == i_index or j == j_index:
                    copy_arr[i][j] = 0
              
   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
    print(result)
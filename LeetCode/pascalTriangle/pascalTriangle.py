class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        bigArray = [[1]]
        for i in range(numRows-1):
            tmp = [0] + bigArray[-1] + [0]
            second_tmp = []
            for j in range(len(bigArray[-1])+1):
                second_tmp.append(tmp[j]+tmp[j+1])
            bigArray.append(second_tmp)
        return bigArray
                
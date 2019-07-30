'''
杨辉三角的每一项等于上一行的上一项加上对应项
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            cur = [0 for x in range(i+1)]
            cur[0]=1
            cur[i]=1
            for j in range(1,len(cur)-1):
                cur[j] = result[i-1][j-1] + result[i-1][j]
            result.append(cur)
        return result

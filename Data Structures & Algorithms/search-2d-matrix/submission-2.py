class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(0,len(matrix)):
            l = 0
            r = len(matrix[i]) - 1
            while l <= r:
                m = (r + l) // 2
                print(l,m,r)
                if matrix[i][m] > target:
                    r = m - 1
                elif matrix[i][m] < target:
                    l = m + 1
                else:
                    return True

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return false

        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m*n - 1
        while l <= r:
            mid = (l + r) // 2
            mi, mj = mid // n, mid % n
            if matrix[mi][mj] == target:
                return True
            elif matrix[mi][mj] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False


            
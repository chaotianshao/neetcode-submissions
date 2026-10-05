class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) // 2

            x = mid // len(matrix[0])
            y = mid % len(matrix[0])

            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                left = left + 1
            else:
                right = right - 1
        return False

        
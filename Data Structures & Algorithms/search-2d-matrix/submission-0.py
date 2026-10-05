class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        colLen = len(matrix[0])
        rowLen = len(matrix)
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) // 2
            row = mid // colLen
            col = mid % colLen

            if matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                return True
        
        return False
            
            
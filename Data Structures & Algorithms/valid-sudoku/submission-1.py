class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeen = [{} for _ in range(9)]
        colSeen = [{} for _ in range(9)]
        boxSeen = [{} for _ in range(9)]
        numRow = 9
        numCol = 9
        for rowIdx in range(numRow):
            for colIdx in range(numCol):
                if board[rowIdx][colIdx] != '.':
                    if board[rowIdx][colIdx] not in rowSeen[rowIdx]:
                        rowSeen[rowIdx][board[rowIdx][colIdx]] = 1
                    else:
                        return False
                    if board[rowIdx][colIdx] not in colSeen[colIdx]:
                        colSeen[colIdx][board[rowIdx][colIdx]] = 1
                    else:
                        return False
                    
                    if board[rowIdx][colIdx] not in boxSeen[rowIdx//3 * 3 + colIdx//3]:
                        boxSeen[rowIdx//3 * 3 + colIdx//3][board[rowIdx][colIdx]]  = 1
                    else:
                        return False
        
        return True
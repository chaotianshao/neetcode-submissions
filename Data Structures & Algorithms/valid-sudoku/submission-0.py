class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashListRow = [[] for _ in range(9)]
        hashListCol = [[] for _ in range(9)]
        hashListSub = [[] for _ in range(9)]

        for rowIdx in range(len(board)):
            for colIdx in range(len(board[rowIdx])):
                if board[rowIdx][colIdx] in hashListRow[rowIdx]:
                    print(hashListRow[rowIdx])
                    return False
                elif board[rowIdx][colIdx] != ".":
                    hashListRow[rowIdx].append(board[rowIdx][colIdx])

                if board[rowIdx][colIdx] in hashListCol[colIdx]:
                    return False
                elif board[rowIdx][colIdx] != ".":
                    hashListCol[colIdx].append(board[rowIdx][colIdx])

                subX = rowIdx // 3
                subY = colIdx // 3

                idx = subX*3+subY
                if board[rowIdx][colIdx] in hashListSub[idx]:
                    return False
                elif board[rowIdx][colIdx] != ".":
                    hashListSub[idx].append(board[rowIdx][colIdx])
        
        return True



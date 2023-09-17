from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 1
        for row in board:
            hashset = set()
            for cell in row:
                if cell != ".":
                    if cell in hashset:
                        print("duplicates!!")
                        return False
                    hashset.add(cell)
                    #print(hashset)
            #print(f"number of the row is {i}. the row is {row}. this is valid")
            i += 1
        
        #print("\n\nnow it is checking the columen")

        for j in range(9):
            column = [board[k][j] for k in range(9)]
            hashset = set()
            for cell in column:
                if cell != ".":
                    if cell in hashset:
                        print("duolicates!!")
                        return False
                    hashset.add(cell)
                    #print(hashset)
            #print(f"column number {j + 1}. the column is {column}")

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                hashset = set()
                for cell in box:
                    if cell != ".":
                        if cell in hashset:
                            return False
                        hashset.add(cell)
        
        return True


solution = Solution()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

solution.isValidSudoku(board)
print(solution.isValidSudoku(board))
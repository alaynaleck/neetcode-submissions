class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        columns = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):

                if board[i][j] == ".":
                    continue

                valIndex = int(board[i][j]) - 1
                
                # Mark the digit has appeared within the row
                if rows[i][valIndex] == True:
                    return False
                rows[i][valIndex] = True;

                # Mark the digit has appeared within the column
                if columns[j][valIndex] == True:
                    return False
                columns[j][valIndex] = True;

                # Mark the digit has appeared within the box
                box = (i//3) * 3 + (j//3)
                if boxes[box][valIndex] == True:
                    return False
                boxes[box][valIndex] = True
            
        return True



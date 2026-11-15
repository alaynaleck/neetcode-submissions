class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row, col, letterIndex):

            if letterIndex == len(word):
                return True
            
            if row not in range(len(board)) or col not in range(len(board[0])):
                return False

            if board[row][col] == '#':
                return False

            if board[row][col] != word[letterIndex]:
                return False
            
            board[row][col] = '#'
            result = (
                dfs(row + 1, col, letterIndex + 1) or
                dfs(row - 1, col, letterIndex + 1) or
                dfs(row, col + 1, letterIndex + 1) or
                dfs(row, col - 1, letterIndex + 1))
            board[row][col] = word[letterIndex]
            return result

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0) == True:
                    return True      
        return False
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        currentSeen = set()
        
        def dfs(row, col, letterIndex):

            if letterIndex == len(word):
                return True
            
            if row not in range(len(board)) or col not in range(len(board[0])):
                return False

            if (row, col) in currentSeen:
                return False

            if board[row][col] != word[letterIndex]:
                return False
            
            currentSeen.add((row, col))
            result = (
                dfs(row + 1, col, letterIndex + 1) or
                dfs(row - 1, col, letterIndex + 1) or
                dfs(row, col + 1, letterIndex + 1) or
                dfs(row, col - 1, letterIndex + 1))
            currentSeen.remove((row, col))
            return result

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0) == True:
                    return True      
        return False
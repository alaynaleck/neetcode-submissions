class Solution:
    def solve(self, board: List[List[str]]) -> None:
        o_edges = set()
        queue = deque()

        def add_o_edge(row, col):
            if (row in range(len(board)) 
                and col in range(len(board[0]))
                and (row, col) not in o_edges
                and board[row][col] == "O"):
                o_edges.add((row, col))
                queue.append((row, col))

        # Initialize the queue for bfs
        for row in range(len(board)):
            add_o_edge(row, 0)
            add_o_edge(row, len(board[0]) - 1)
        for col in range(len(board[0])):
            add_o_edge(0, col)
            add_o_edge(len(board) - 1, col)

        while queue:
            row, col = queue.popleft()
            
            add_o_edge(row - 1, col)
            add_o_edge(row + 1, col)
            add_o_edge(row, col - 1)
            add_o_edge(row, col + 1)

        # Anything that cannot be reached by the queue we can capture
        for row in range(len(board)):
            for col in range(len(board[0])):
                # Capture all non-edge and non-boardered regions
                if (row != 0 and row != len(board) - 1
                    and col != 0 and col != len(board[0]) - 1
                    and (row, col) not in o_edges):
                    board[row][col] = "X"
        
        return 
        

        
            
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                cell = board[row][col]
                if cell in rows[row] or cell in cols[col] or cell in squares[(row//3, col//3)]:
                    return False

                rows[row].add(cell)
                cols[col].add(cell)
                squares[(row//3, col//3)].add(cell)

        return True
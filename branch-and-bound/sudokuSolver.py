def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r//3)*3 + c//3].add(val)

        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r+1, 0)
            if board[r][c] != ".":
                return backtrack(r, c+1)

            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[(r//3)*3 + c//3]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r//3)*3 + c//3].add(num)

                    if backtrack(r, c+1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[(r//3)*3 + c//3].remove(num)

            return False

        backtrack(0, 0)
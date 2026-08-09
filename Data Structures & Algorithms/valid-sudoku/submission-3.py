class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        square = {}

        for r in range(9):
            for c in range(9):
                ele = board[r][c]
                if ele == ".":
                    continue
                if c not in cols:
                    cols[c] = set()
                if r not in rows:
                    rows[r] = set()
                if (r // 3, c // 3) not in square:
                    square[(r // 3, c // 3)] = set()

                if ((ele in cols[c]) or
                    (ele in rows[r]) or
                    (ele in square[(r // 3, c // 3)])):

                    return False
                else:
                    cols[c].add(ele)
                    rows[r].add(ele)
                    square[(r // 3, c // 3)].add(ele)

        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROW  = len(board)
        COL =  len(board[0])

        res = []
        def backtracking(r,c,i):
            if  i == len(word):
                return True
            
            if  (r >= ROW or c >= COL or r < 0 or c < 0 or board[r][c] != word[i]):
                     return False
            
            board[r][c] = '*'
            ret = (backtracking(r + 1, c, i + 1) or 
                   backtracking(r - 1, c, i + 1) or 
                   backtracking(r, c + 1, i + 1) or 
                   backtracking(r, c - 1, i + 1) )
            board[r][c] = word[i]
            return ret

        for word in words:
            flag = False
            for r in range (ROW):
                if flag:
                    break
                for c in range (COL):
                    if board[r][c] != word[0]:
                        continue
                    if  backtracking(r,c,0):
                        res.append(word)
                        flag = True
                        break
        return res

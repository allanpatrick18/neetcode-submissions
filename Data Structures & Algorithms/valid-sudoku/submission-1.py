class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        pace = 3
        row = 0
        m = 0
        for i in range(0,9):
            line = {}
            col = {}
            cell = {}
            if i >=pace:
                row += 1
                pace = pace + 3
            if m >=9:
                m = 0
            index = row*3
            print(row,index,pace)
            for j in range(0,9):
                if board[i][j] in line:
                    print('line')
                    print(line)
                    return False
                elif board[i][j] != '.':
                    line[board[i][j]] = None

                if board[j][i] in col:
                    print('col')
                    print(col)
                    return False
                elif board[j][i] != '.':
                    col[board[j][i]] = None
                
                if index >= row*3 + 3:
                    index = row*3
                    m +=1
                print(m,index)  
                if board[m][index] in cell:
                    print('cell')
                    print(cell)
                    return False
                elif board[m][index] != '.':
                    cell[board[m][index]] = None
                
                index +=1

            m +=1
            print('----')
        return True

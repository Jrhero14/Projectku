import time
step = 0
semiGrid = [[],[],[],[],[],[],[],[],[]]
grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

with open("D:/Project/Sudoku/Sudoku.txt") as f:
    for i in range(9):
        semiGrid[i] = list(f.readline())
    for i in range(9):
        for j in range(9):
            grid[i][j] = int(semiGrid[i][j])
    f.close()

def countSolved():
    global grid
    for i in range(9):
        if (0 in grid[i]):
            return True
    return False

def possible(x,y,n):
    global grid
    for a in range(9):
        if (grid[x][a] == n):
            return False
    for b in range(9):
        if (grid[b][y] == n):
            return False
    Xo = (x//3)*3
    Yo = (y//3)*3
    for i in range(3):
        for j in range(3):
            if(grid[Xo+i][Yo+j] == n):
                return False

    return True

def SudokuPattern():
    print(" "+str(grid[0][0]) + " " + str(grid[0][1]) + " " + str(grid[0][2]) + " |" + " " + str(grid[0][3]) + " " + str(grid[0][4]) + " " + str(grid[0][5]) + " |" + " " + str(grid[0][6]) + " " + str(grid[0][7]) + " " + str(grid[0][8]))
    print(" "+str(grid[1][0]) + " " + str(grid[1][1]) + " " + str(grid[1][2]) + " |" + " " + str(grid[1][3]) + " " + str(grid[1][4]) + " " + str(grid[1][5]) + " |" + " " + str(grid[1][6]) + " " + str(grid[1][7]) + " " + str(grid[1][8]))
    print(" "+str(grid[2][0]) + " " + str(grid[2][1]) + " " + str(grid[2][2]) + " |" + " " + str(grid[2][3]) + " " + str(grid[2][4]) + " " + str(grid[2][5]) + " |" + " " + str(grid[2][6]) + " " + str(grid[2][7]) + " " + str(grid[2][8]))
    print("-------+-------+-------")
    print(" "+str(grid[3][0]) + " " + str(grid[3][1]) + " " + str(grid[3][2]) + " |" + " " + str(grid[3][3]) + " " + str(grid[3][4]) + " " + str(grid[3][5]) + " |" + " " + str(grid[3][6]) + " " + str(grid[3][7]) + " " + str(grid[3][8]))
    print(" "+str(grid[4][0]) + " " + str(grid[4][1]) + " " + str(grid[4][2]) + " |" + " " + str(grid[4][3]) + " " + str(grid[4][4]) + " " + str(grid[4][5]) + " |" + " " + str(grid[4][6]) + " " + str(grid[4][7]) + " " + str(grid[4][8]))
    print(" "+str(grid[5][0]) + " " + str(grid[5][1]) + " " + str(grid[5][2]) + " |" + " " + str(grid[5][3]) + " " + str(grid[5][4]) + " " + str(grid[5][5]) + " |" + " " + str(grid[5][6]) + " " + str(grid[5][7]) + " " + str(grid[5][8]))
    print("-------+-------+-------")
    print(" "+str(grid[6][0]) + " " + str(grid[6][1]) + " " + str(grid[6][2]) + " |" + " " + str(grid[6][3]) + " " + str(grid[6][4]) + " " + str(grid[6][5]) + " |" + " " + str(grid[6][6]) + " " + str(grid[6][7]) + " " + str(grid[6][8]))
    print(" "+str(grid[7][0]) + " " + str(grid[7][1]) + " " + str(grid[7][2]) + " |" + " " + str(grid[7][3]) + " " + str(grid[7][4]) + " " + str(grid[7][5]) + " |" + " " + str(grid[7][6]) + " " + str(grid[7][7]) + " " + str(grid[7][8]))
    print(" "+str(grid[8][0]) + " " + str(grid[8][1]) + " " + str(grid[8][2]) + " |" + " " + str(grid[8][3]) + " " + str(grid[8][4]) + " " + str(grid[8][5]) + " |" + " " + str(grid[8][6]) + " " + str(grid[8][7]) + " " + str(grid[8][8]))

def solve():
    global grid
    global step
    for i in range(9):
        for j in range(9):
            if (grid[i][j] == 0):
                for k in range(1,10):
                    if (possible(i,j,k)):
                        grid[i][j] = k
                        step += 1
                        SudokuPattern()
                        print(" ")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~ Step:" + str(step))
                        if (countSolved() == False):
                            SudokuPattern()
                            print(" ~~~~~~ Solved ~~~~~~~")
                            quit()
                        solve()
                        grid[i][j] = 0
                return
print("Sudoku Solver by Jeremi Hero")
SudokuPattern()
print(" ")
input("[enter] untuk menyelesaikan...")
solve()

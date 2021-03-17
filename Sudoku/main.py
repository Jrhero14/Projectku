import time
k1 = [0,0,0]
k2 = [0,0,0]
k3 = [0,0,0]
sudokuB = [[0,0,0],[0,0,0],[0,0,0]]
sudokuC = [[0,0,0],[0,0,0],[0,0,0]]
elementEx = 9
with open("D:/Project/Sudoku/Sudoku.txt") as f:
    b1 = list(f.readline())
    del b1[3]
    for i in range(3):
        if(b1[i] == "."):
            sudokuB[0][i] = 0
            elementEx -= 1
        else:
            sudokuB[0][i] = int(b1[i])

    b2 = list(f.readline())
    del b2[3]
    for i in range(3):
        if (b2[i] == "."):
            sudokuB[1][i] = 0
            elementEx -= 1
        else:
            sudokuB[1][i] = int(b2[i])

    b3 = list(f.readline())
    for i in range(3):
        if (b3[i] == "."):
            sudokuB[2][i] = 0
            elementEx -= 1
        else:
            sudokuB[2][i] = int(b3[i])
    f.close()

for i  in range(3):
    for j in range(3):
        sudokuC[i][j] = sudokuB[j][i]
print("Simple Sudoku 3x3 Solving by Jeremi Hero")
print("Case:")
print("",sudokuB[0],"\n",sudokuB[1],"\n",sudokuB[2])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Solving algorithm
print("~~~~~~~~~~~~~~~~~~~ Solving")
input("[Enter] untuk menyelesaikan...")
print("",sudokuB[0],"\n",sudokuB[1],"\n",sudokuB[2])

while (elementEx < 9):
    for i in range(3):
        for j in range(3):
            if (sudokuB[i][j] == 0):
                for k in range(1,4):
                    if ((k in sudokuB[i]) == (k in sudokuC[j]) == False):
                        sudokuB[i][j] = k
                        sudokuC[j][i] = k
                        elementEx += 1
                        time.sleep(0.3)
                        print(" ")
                        print("", sudokuB[0], "\n", sudokuB[1], "\n", sudokuB[2])
                        break
            else:
                continue
print("~~~~~~~~~~~~~~~~~~~~")
print("Solved:")
print("",sudokuB[0],"\n",sudokuB[1],"\n",sudokuB[2])
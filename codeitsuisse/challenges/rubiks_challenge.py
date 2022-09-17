from copy import deepcopy

def rubiks(ops:str, state:dict):
    commands = processCommands(ops)
    for command in commands:
        if command == "U":
            rotateRow(0, state)
        elif command == "Ui":
            rotateRowAnti(0, state)
        elif command == "L":
            rotateCol(0, state)
        elif command == "Li":
            rotateCol(0, state)
        elif command == "F":
            rotateCross(0, state)
        elif command == "Fi":
            rotateCrossAnti(0, state)
        elif command == "R":
            rotateCol(2, state)
        elif command == "Ri":
            rotateColAnti(2, state)
        elif command == "B":
            rotateCross(2, state)
        elif command == "Bi":
            rotateCrossAnti(2, state)
        elif command == "D":
            rotateRow(2, state)
        elif command == "Di":
            rotateRowAnti(0, state)
    return state

def rotateCross(row:int, state:dict):
    # Put up row 1 into right col 3
    tempR = deepcopy(state["r"])
    for i in range(0, 3):
        state["r"][i][2-row] = state["u"][row][i]
    # Put right col 3 into down row 3
    # Need to reverse after
    tempD = deepcopy(state["d"])
    for i in range(0, 3):
        state["d"][2-row][i] = tempR[i][row]
    state["d"][2-row] = state["d"][2-row].reverse()
    # Put down row 3 into left col 1
    tempL = deepcopy(state["l"])
    for i in range(0, 3):
        state["l"][i][row] = tempD[2-row][i]
    # Put left col 3 into up row 1
    for i in range(0, 3):
        state["u"][row][i] = tempL[i][2-row]
    state["u"][row] = state["u"].reverse()
    if row == 0:
        state = rotateFace("f", state)
    else:
        state = rotateFace("b", state)
    return state    

def rotateCrossAnti(row:int, state:dict):
    # Put up row 1 into left col 3
    tempL = deepcopy(state["l"])
    for i in range(0, 3):
        state["l"][i][2-row] = state["u"][row][i]
    # Put left col 3 into down row 3
    # Need to reverse after
    tempD = deepcopy(state["d"])
    for i in range(0, 3):
        state["d"][2-row][i] = tempL[i][row]
    state["d"][2-row] = state["d"][2-row].reverse()
    # Put down row 3 into right col 1
    tempR = deepcopy(state["r"])
    for i in range(0, 3):
        state["r"][i][row] = tempD[2-row][i]
    # Put right col 3 into up row 1
    for i in range(0, 3):
        state["u"][row][i] = tempR[i][2-row]
    state["u"][row] = state["u"].reverse()
    if row == 0:
        state = rotateFaceAnti("f", state)
    else:
        state = rotateFaceAnti("b", state)
    return state    

def rowToCol(dest:list[list[int]], src:list[list[int]], destRow:int, srcRow:int):
    for i in range(0, 3):
        dest[destRow][i] = src[srcRow][i]
    return dest

# front top row becomes right top row
# right top row becomes back top row
# back top row becomes left top row
# left top row becomes front top row
def rotateRow(row:int, state:dict):
    tempR = list(state["r"][row])
    tempB = list(state["b"][row])
    tempL = list(state["l"][row])
    tempF = list(state["f"][row])
    state["r"][row] = tempF
    state["b"][row] = tempR
    state["l"][row] = tempB
    state["f"][row] = tempL
    if row == 2:
        state = rotateFace("d", state)
    elif row == 0:
        state = rotateFace("u", state)
    return state

def rotateRowAnti(row:int, state:dict):
    tempR = list(state["r"][row])
    tempB = list(state["b"][row])
    tempL = list(state["l"][row])
    tempF = list(state["f"][row])
    state["f"][row] = tempR
    state["l"][row] = tempF
    state["b"][row] = tempL
    state["r"][row] = tempB
    if row == 2:
        state = rotateFaceAnti("d", state)
    elif row == 0:
        state = rotateFaceAnti("u", state)
    return state

def transposeCol(dest:list[list[int]], src:list[list[int]], destCol:int, srcCol:int):
    temp = deepcopy(dest)
    for i in range(0, 3):
        dest[i][destCol] = src[i][srcCol]
    return temp

def reverseCol(f:str, col:int, state:dict):
    temp = state[f][0][2-col]
    state[f][0][2-col] = state[f][2][2-col]
    state[f][2][2-col] = temp
    return state

def rotateCol(col:int, state:dict):
    tempF = transposeCol(state["f"], state["t"], col, col)
    tempD = transposeCol(state["d"], tempF, col, col)
    tempB = transposeCol(state["b"], tempD, col, 2 - col)
    # Reverse the back column
    state = reverseCol("b", col, state)
    transposeCol(state["t"], tempB, 2 - col, col)
    # Reverse the top column
    state = reverseCol("t", col, state)
    # Rotate faces
    if col == 2:
        state = rotateFace("r", state)
    elif col == 0:
        state = rotateFace("l", state)
    return state

def rotateColAnti(col:int, state:dict):
    tempT = transposeCol(state["t"], state["f"], col, col)
    tempB = transposeCol(state["b"], tempT, col, col)
    # Reverse back column
    state = reverseCol("b", col, state)    
    tempD = transposeCol(state["d"], tempB, col, 2 - col)
    # Reverse the bottom column
    state = reverseCol("d", col, state)    
    transposeCol(state["f"], tempD, 2 - col, col)
    # Rotate faces
    if col == 2:
        state = rotateFaceAnti("r", state)
    elif col == 0:
        state = rotateFaceAnti("l", state)
    return state

# Top row becomes left col
# Left col becomes bottom row
# bottom row becomes right col
# right col becomes top row
def rotateFace(faceName: str, state:dict):
    matrix = state[faceName]
    # Flip Vertically
    for i in range(len(matrix)):
        for j in range(len(matrix) // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
    # Flip Diagonally
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    state[faceName] = matrix
    return state

def rotateFaceAnti(faceName: str, state:dict):
    matrix = state[faceName]
    # Flip Vertically
    for i in range(len(matrix)):
        matrix[i].reverse()
    # Flip Diagonally
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    state[faceName] = matrix
    return state

def processCommands(ops:str):
    res = []
    index = len(ops) - 1
    while index >= 0:
        if (ops[index] == 'i'):
            res.insert(ops[index-1] + ops[index])
            index -= 1
        index -= 1
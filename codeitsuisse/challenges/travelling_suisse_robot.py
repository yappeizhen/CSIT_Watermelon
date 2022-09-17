import itertools
def read_maze(maze: str):
    y = maze.split("\n")[:-1]
    positions = dict()
    positions["S"], positions["E"], positions["I"] = [], [], []
    for row in range(len(y)):
        for col in range(len(y[row])):
            if y[row][col] == " ":
                continue
            if y[row][col] != "E" and y[row][col] != "S" and y[row][col] != "I":
                positions[y[row][col]] = (row, col)
            else:
                positions[y[row][col]].append((row, col))
    min_dist = float("inf")
    min_esi_perm = []
    for e_perms in itertools.permutations(positions["E"]):
        for s_perms in itertools.permutations(positions["S"]):
            for i_perms in itertools.permutations(positions["I"]):
                curr_dist = 0
                curr_esi_perm = [e_perms, s_perms, i_perms]
                curr_dist += get_distance(e_perms[0], i_perms[0])
                curr_dist += get_distance(i_perms[0], positions["T"])
                curr_dist += get_distance(positions["T"], s_perms[0])
                curr_dist += get_distance(s_perms[0], positions["U"])
                curr_dist += get_distance(positions["U"], i_perms[1])
                curr_dist += get_distance(i_perms[1], s_perms[1])
                curr_dist += get_distance(s_perms[1], s_perms[2])
                curr_dist += get_distance(s_perms[2], e_perms[1])
                if curr_dist < min_dist:
                    min_dist = curr_dist
                    min_esi_perm = curr_esi_perm

    face, xc = a_to_b(positions["X"], positions["C"], "u")
    face, co = a_to_b(positions["C"], positions["O"], face)
    face, od = a_to_b(positions["O"], positions["D"], face)
    face, de = a_to_b(positions["D"], min_esi_perm[0][0], face)
    face, ei = a_to_b(min_esi_perm[0][0], min_esi_perm[2][0], face)
    face, it = a_to_b(min_esi_perm[2][0], positions["T"], face)
    face, ts = a_to_b(positions["T"], min_esi_perm[1][0], face)
    face, su = a_to_b(min_esi_perm[1][0], positions["U"], face)
    face, ui = a_to_b(positions["U"], min_esi_perm[2][1], face)
    face, is_str = a_to_b(min_esi_perm[2][1], min_esi_perm[1][1], face)
    face, ss = a_to_b(min_esi_perm[1][1], min_esi_perm[1][2], face)
    face, se = a_to_b(min_esi_perm[1][2], min_esi_perm[0][1], face)

    final_str = xc + co + od + de + ei + it + ts + su + ui + is_str + ss + se
    return final_str

def get_vert(d):
    i = "S" * abs(d[0])
    return i

def get_horizontal(d):
    i = "S" * abs(d[1])
    return i

def a_to_b(a: tuple, b: tuple, face: str):
    toReturn = ""
    d = (b[0]-a[0], b[1]-a[1])
    if d[0] < 0 and face == "u":
        toReturn = get_vert(d)
        if d[1] > 0:
            toReturn += "R"
            face = 'r'
        elif d[1] < 0:
            toReturn += "L"
            face = 'l'
        toReturn += get_horizontal(d)    
    elif d[0] > 0 and face == "d":
        toReturn = get_vert(d)
        if d[1] > 0:
            toReturn += "L"
            face = 'l'
        elif d[1] < 0:
            toReturn += "R"
            face = 'r'
        toReturn += get_horizontal(d)
    elif d[1] > 0 and face == "r":
        toReturn = get_horizontal(d)
        if d[0] < 0:
            toReturn += "L"
            face = 'u'
        elif d[0] > 0:
            toReturn += "R"
            face = 'd'
        toReturn += get_vert(d)
    elif d[1] < 0 and face == "l":
        toReturn = get_horizontal(d)
        if d[0] < 0:
            toReturn += "R"
            face = 'u'
        elif d[0] > 0:
            toReturn += "L"
            face = 'd'
        toReturn += get_vert(d)
    else:
        if face == "l" and d[0] < 0:
            toReturn += "R"
            toReturn += get_vert(d)
            if d[1] != 0:
                toReturn += "R"
                face = 'r'
            else:
                face = 'u'
            toReturn += get_horizontal(d)
        elif face == "l" and d[0] > 0:
            toReturn += "L"
            toReturn += get_vert(d)
            if d[1] != 0:
                toReturn += "L"
                face = 'r'
            else: 
                face = 'd'
            toReturn += get_horizontal(d)
        elif face == "r" and d[0] > 0:
            toReturn += "R"
            toReturn += get_vert(d)
            if d[1] != 0:
                toReturn += "R"
                face = 'l'
            else:
                face = "d"
            toReturn += get_horizontal(d)
        elif face == "r" and d[0] < 0:
            toReturn += "L"
            toReturn += get_vert(d)
            if d[1] != 0:
                toReturn += "L"
                face = 'l'
            else:
                face = 'u'
            toReturn += get_horizontal(d)
        elif face == "u" and d[1] > 0:
            toReturn += "R"
            toReturn += get_horizontal(d)
            if d[0] != 0:
                toReturn += "R"
                face = 'd'
            else:
                face = 'r'
            toReturn += get_vert(d)
        elif face == "u" and d[1] < 0:
            toReturn += "L"
            toReturn += get_horizontal(d)
            if d[0] != 0:
                toReturn += "L"
                face = 'd'
            else:
                face = 'l'
            toReturn += get_vert(d)
        elif face == "d" and d[1] > 0:
            toReturn += "L"
            toReturn += get_horizontal(d)
            if d[0] != 0:
                toReturn += "L"
                face = 'u'
            else:
                face = 'r'
            toReturn += get_vert(d)
        elif face == "d" and d[1] < 0:
            toReturn += "R"
            toReturn += get_horizontal(d)
            if d[0] != 0:
                toReturn += "R"
                face = 'u'
            else:
                face = 'l'
            toReturn += get_vert(d)
    toReturn += "P"
    return (face, toReturn)

def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

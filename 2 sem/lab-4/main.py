import random
import turtle
import math

class Vertex:
    def __init__(self, pos_x, pos_y, num):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.num = num

def print_matrix(matrix):
    for row in range(len(matrix)):
        print(matrix[row])

def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def create_random_matrix(seed, len_matrix):
    random.seed(seed)
    return [[random.uniform(0, 2.0) for _ in range(len_matrix)] for _ in range(len_matrix)]

def multiply_matrix_on_k(matrix, k):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= k
    return matrix

def rounding_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = math.floor(matrix[i][j])
    return matrix

def undirecting_matrix(dirmatrix):
    undirmatrix = [[0 for _ in range(len(dirmatrix))] for _ in range(len(dirmatrix))]
    for i in range(len(dirmatrix)):
        for j in range(len(dirmatrix)):
            if dirmatrix[i][j]:
                undirmatrix[i][j] = 1
                undirmatrix[j][i] = 1
    return undirmatrix

def matrix_multiply(matrixA, matrixB):
    n = len(matrixA)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
    return result

def add_matrix(matrixA, matrixB):
    return [[matrixA[i][j] + matrixB[i][j] for j in range(len(matrixA[0]))] for i in range(len(matrixA))]

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def dfs(strong_matrix, vertex, component, visited):
    visited[vertex] = True
    component[vertex] = 1
    for i in range(len(strong_matrix)):
        if (not visited[i]) and strong_matrix[vertex][i]:
            dfs(strong_matrix, i, component, visited)

def element_multiply_matrix(matrixA, matrixB):
    return [[matrixA[i][j] * matrixB[i][j] for j in range(len(matrixA[0]))] for i in range(len(matrixB))]
def boolean_transformation_matrix(matrix):
    return [[1 if matrix[i][j] else 0 for j in range(len(matrix))] for i in range(len(matrix))]

def matrix_power(matrix, power):
    n = len(matrix)
    result = [[0 if row != col else 1 for col in range(n)] for row in range(n)]
    while power > 0:
        if power % 2 == 1:
            result = matrix_multiply(result, matrix)
        matrix = matrix_multiply(matrix, matrix)
        power //= 2
    return result

def power_of_vertexes(matrix, isDir):
    powers = []
    for i in range(len(matrix)):
        power = 0
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                power += 1
                if not isDir:
                    if i == j:
                        power += 1
            if isDir:
                if matrix[j][i]:
                    power += 1
        powers.append(power)
        print(f'Power of vertex {i+1} is {power}')
    return powers

def half_power_of_vertexes(matrix):
    for i in range(len(matrix)):
        input_power = 0
        output_power = 0
        for j in range(len(matrix)):
            if matrix[i][j]:
                output_power += 1
            if matrix[j][i]:
                input_power += 1
        print(f'VERTEX {i+1} Half power of input: {input_power} output:{output_power}')

def isolated_hanged_homogeneous_vertexes(powers):
    count_of_iso = 0
    count_of_hanged = 0
    num = 1
    for power in powers:
        if power == 0:
            count_of_iso += 1
            print(f'Vertex {num} is isolated')
        if power == 1:
            count_of_hanged += 1
            print(f'Vertex {num} is hanged')
        num += 1
    if count_of_iso == 0:
        print('No isolated vertexes')
    if count_of_hanged == 0:
        print('No hanged vertexes')
    if all(x == powers[0] for x in powers):
        print(f'Vertexes is homogeneous power of {powers[0]}')
    else:
        print('Vertexes is not homogeneous')

def paths_of_length_2_and_3_of_vertexes(adjmatrix):
    n = len(adjmatrix)
    adjmatrixpower2 = [[0 for _ in range(n)] for _ in range(n)]
    adjmatrixpower3 = [[0 for _ in range(n)] for _ in range(n)]
    pathslen2 = []
    pathslen3 = []
    for i in range(n):
        for j in range(n):
            if adjmatrix[i][j] == 1:
                for k in range(n):
                    if adjmatrix[j][k] == 1:
                        adjmatrixpower2[i][k] += 1
                        pathslen2.append([i+1, j+1, k+1])
                        for x in range(n):
                            if adjmatrix[k][x] == 1:
                                adjmatrixpower3[i][x] += 1
                                pathslen3.append([i + 1, j + 1, k + 1, x + 1])
    print('\n-----Adjacency matrix power of 2-----')
    print_matrix(adjmatrixpower2)
    print('\nPaths of length 2:')
    for path in range(len(pathslen2)):
        print(pathslen2[path])
    print('\n-----Adjacency matrix power of 3-----')
    print_matrix(adjmatrixpower3)
    print('\nPaths of length 3:')
    for path in range(len(pathslen3)):
        print(pathslen3[path])

def reachability_matrix(adjmatrix):
    reach_matrix = adjmatrix
    for i in range(2, len(reach_matrix) - 1):
        reach_matrix = add_matrix(reach_matrix, matrix_power(adjmatrix, i))
    reach_matrix = add_matrix(reach_matrix, identity_matrix(len(reach_matrix)))
    reach_matrix = boolean_transformation_matrix(reach_matrix)
    return reach_matrix

def matrix_strong_connectivity(reach_matrix):
    return element_multiply_matrix(reach_matrix, transpose_matrix(reach_matrix))

def components_of_strong_connectivity(strong_matrix):
    n = len(strong_matrix)
    visited = [False] * n
    components_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for vertex in range(n):
        if not visited[vertex]:
            dfs(strong_matrix, vertex, components_matrix[vertex], visited)

    components = []
    for i in range(len(components_matrix)):
        temp = []
        if components_matrix[i][i]:
            for j in range(len(components_matrix[i])):
                if components_matrix[i][j]:
                    temp.append(j + 1)
            components.append(temp)

    for i in range(len(components)):
        print(f'Component {i + 1}: {components[i]}')
    return components

def condensation_matrix(adjmatrix, components):
    count_of_vertexes = len(components)
    condensation_matrix = [[0] * count_of_vertexes for _ in range(count_of_vertexes)]
    for i in range(len(adjmatrix)):
        for j in range(len(adjmatrix[i])):
            if adjmatrix[i][j]:
                index_com_i = next(index for index, com in enumerate(components) if i + 1 in com)
                index_com_j = next(index for index, com in enumerate(components) if j + 1 in com)
                if index_com_i != index_com_j:
                    condensation_matrix[index_com_i][index_com_j] = 1
    return condensation_matrix

def position_of_vertex(amount):
    vertex = []
    x = -350
    y = 200
    for i in range(amount):
        if i < amount / 2 - 1:
            x += 150
            vertex.append(Vertex(x, y, i))
        elif i >= amount / 2 - 1 and i < amount / 2 + 1:
            y -= 150
            vertex.append(Vertex(x, y, i))
        elif i >= amount / 2 + 1 and i < amount - 1:
            x -= 150
            vertex.append(Vertex(x, y, i))
        elif i >= amount - 1:
            y += 150
            vertex.append(Vertex(x, y, i))
    return vertex

def drawing_vertex(vertex): #Малювання вершин
    turtle.setheading(0)
    for i in range(len(vertex)):
        turtle.up()
        turtle.color('blue')
        turtle.goto(vertex[i].pos_x, vertex[i].pos_y)
        turtle.down()
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()
        turtle.color('white')
        turtle.write(f"{vertex[i].num+1}", False, 'center', ('Arial', 20, 'normal'))
        turtle.color('black')

def draw_loop(x, y, isDir):
    turtle.up()
    turtle.goto(x, y + 20)
    angle = math.atan2(y - 50, x - 25) * 180 / math.pi
    turtle.setheading(angle + 270)
    turtle.down()
    turtle.circle(25, 313)
    if isDir:
        turtle.stamp()

def draw_line(x1, y1, x2, y2, isDir):
    turtle.up()
    turtle.goto(x1, y1 + 20)
    angle = math.atan2(y2 - y1, x2 - x1) * 180 / math.pi
    turtle.setheading(angle)
    turtle.down()
    turtle.goto(x2, y2 + 20)
    if isDir:
        turtle.backward(20)
        turtle.stamp()

def draw_up_arc(x1, y1, x2, y2, isDir, e):
    turtle.up()
    turtle.goto(x1, y1+20)
    turtle.down()
    turtle.goto((x1 + x2)/2, y2+e)
    draw_line((x1 + x2)/2, y2+e-20, x2, y2, isDir)

def draw_down_arc(x1, y1, x2, y2, isDir, e):
    turtle.up()
    turtle.goto(x1, y1 + 20)
    turtle.down()
    turtle.goto((x1 + x2) / 2, y2 - e)
    draw_line((x1 + x2) / 2, y2 - e-20, x2, y2, isDir)

def draw_left_arc(x1, y1, x2, y2, isDir,e):
    turtle.up()
    turtle.goto(x1, y1 + 20)
    turtle.down()
    turtle.goto(x2 - e, (y1 + y2) / 2 + 20)
    draw_line(x2 - e, (y1 + y2) / 2, x2, y2, isDir)

def draw_right_arc(x1, y1, x2, y2, isDir,e):
    turtle.up()
    turtle.goto(x1, y1 + 20)
    turtle.down()
    turtle.goto(x2 + e, (y1 + y2) / 2 + 20)
    draw_line(x2 + e, (y1 + y2) / 2, x2, y2, isDir)
def draw_connection_vertex(vertex, matrix, isDir):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            elevate = 70
            if matrix[i][j]:
                if matrix[i][j] == matrix[j][i] and isDir and vertex[i].num > vertex[j].num:
                    elevate = elevate * 2 - 10
                if j == i:
                    draw_loop(vertex[i].pos_x, vertex[i].pos_y, isDir)
                elif vertex[i].pos_y == vertex[j].pos_y and abs(vertex[i].pos_x - vertex[j].pos_x) > 150 and (vertex[i].pos_y == 200 or vertex[i].pos_y == -100):
                    if vertex[i].pos_y == 200:
                        draw_up_arc(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, isDir, elevate)
                    if vertex[i].pos_y == -100:
                        draw_down_arc(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, isDir, elevate)

                elif vertex[i].pos_x == vertex[j].pos_x and abs(vertex[i].pos_y - vertex[j].pos_y) > 150 and (vertex[i].pos_x == -200 or vertex[i].pos_x == 250):
                    if vertex[i].pos_x == -200:
                        draw_left_arc(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, isDir, elevate)
                    elif vertex[i].pos_x == 250:
                        draw_right_arc(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, isDir, elevate)

                else:
                    if matrix[i][j] == matrix[j][i] and isDir and vertex[i].num > vertex[j].num:
                        draw_line(vertex[i].pos_x, vertex[i].pos_y, (vertex[i].pos_x + vertex[j].pos_x) / 2 + 20, (vertex[i].pos_y + vertex[j].pos_y) / 2 - 20, False)
                        draw_line((vertex[i].pos_x + vertex[j].pos_x) / 2 + 20, (vertex[i].pos_y + vertex[j].pos_y) / 2 - 20, vertex[j].pos_x, vertex[j].pos_y, isDir)

                    else:
                        draw_line(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, isDir)

def display_message(message):
    turtle.up()
    turtle.goto(-200, -300)
    turtle.down()
    turtle.write(message, False, 'center', ('Arial', 20, 'normal'))

def switch_graph(graph_type, direct_matrix, undirect_matrix, adjacency_matrix, consd_matrix):
    if graph_type == 'direct':
        vertex_pos = position_of_vertex(len(direct_matrix))
        draw_connection_vertex(vertex_pos, direct_matrix, True)
        drawing_vertex(vertex_pos)
        display_message("Direction Graph, Press SPACE to switch")
    elif graph_type == 'undirect':
        vertex_pos = position_of_vertex(len(undirect_matrix))
        draw_connection_vertex(vertex_pos, undirect_matrix, False)
        display_message("Undirection Graph, Press SPACE to switch")
        drawing_vertex(vertex_pos)
    elif graph_type == 'adjacency':
        vertex_pos = position_of_vertex(len(adjacency_matrix))
        draw_connection_vertex(vertex_pos, adjacency_matrix, True)
        drawing_vertex(vertex_pos)
        display_message("Adjacency Graph, Press SPACE to switch")
    elif graph_type == 'condensation':
        vertex_pos = position_of_vertex(len(consd_matrix))
        draw_connection_vertex(vertex_pos, consd_matrix, True)
        drawing_vertex(vertex_pos)
        display_message("Condensation Graph, Press SPACE to switch")

num = 0
def switch(direct_matrix, undirect_matrix, adjacency_matrix, consd_matrix):
    global num
    turtle.clear()
    num += 1
    if num > 4:
        num = 1
    switch_cases = {
        1: 'direct',
        2: 'undirect',
        3: 'adjacency',
        4: 'condensation'
    }
    graph_type = switch_cases[num]
    switch_graph(graph_type, direct_matrix, undirect_matrix, adjacency_matrix, consd_matrix)

def main():
    n3 = 0
    n4 = 2
    n = 10
    seed = 3202
    k = 1 - n3 * 0.01 - n4 * 0.01 - 0.3
    turtle.speed(0)

    matrix = create_random_matrix(seed, n)
    matrix = multiply_matrix_on_k(matrix, k)
    direct_matrix = rounding_matrix(matrix)
    print('-----Direction matrix-----')
    print_matrix(direct_matrix)
    print('-----Undirection matrix-----')
    undirect_matrix = undirecting_matrix(direct_matrix)
    print_matrix(undirect_matrix)
    print('\nPower of direct vertexes:')
    dirpowers = power_of_vertexes(direct_matrix, True)
    print('\nPower of undirect vertexes:')
    undirpowers = power_of_vertexes(undirect_matrix, False)
    print('\nHalf powers of direct vertexes:')
    half_power_of_vertexes(direct_matrix)
    print('\nDirect Vertexes:')
    isolated_hanged_homogeneous_vertexes(dirpowers)
    print('\nUndirect Vertexes:')
    isolated_hanged_homogeneous_vertexes(undirpowers)
    k = 1 - n3 * 0.005 - n4 * 0.005 - 0.27
    adjacency_matrix = create_random_matrix(seed, n)
    adjacency_matrix = multiply_matrix_on_k(adjacency_matrix, k)
    adjacency_matrix = rounding_matrix(adjacency_matrix)
    print('\n-----Adjacency matrix-----')
    print_matrix(adjacency_matrix)
    print('\nHalf powers of adjacency vertexes:')
    half_power_of_vertexes(adjacency_matrix)
    paths_of_length_2_and_3_of_vertexes(adjacency_matrix)
    reach_matrix = reachability_matrix(adjacency_matrix)
    print('\n-----Reachability matrix-----')
    print_matrix(reach_matrix)
    strong_matrix = matrix_strong_connectivity(reach_matrix)
    print('\n-----Strong Connectivity Matrix-----')
    print_matrix(strong_matrix)
    print('\nComponents of strong connectivity:')
    components = components_of_strong_connectivity(strong_matrix)
    consd_matrix = condensation_matrix(adjacency_matrix, components)
    print('\n-----Condensation Matrix-----')
    print_matrix(consd_matrix)

    turtle.up()
    turtle.goto(-200, -300)
    turtle.down()
    turtle.write("Press SPACE to start", False, 'center', ('Arial', 20, 'normal'))
    turtle.listen()
    turtle.onkey(lambda: switch(direct_matrix, undirect_matrix, adjacency_matrix, consd_matrix), "space")
    turtle.mainloop()



main()
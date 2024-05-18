import random
import turtle
import math
import keyboard

V_RADIUS = 20
CENTER_X = 25
CENTER_Y = 50
DISTANCE_BETWEEN_V = 150
UP_SIDE_Y = 200
DOWN_SIDE_Y = -100
LEFT_SIDE_X = -200
RIGHT_SIDE_X = 250
ELEVATE = 80


class Vertex:
    def __init__(self, pos_x, pos_y, num):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.num = num


class Edge:
    def __init__(self, weight, edge_from, edge_to):
        self.weight = weight
        self.edge_from = edge_from
        self.edge_to = edge_to


class List:
    def __init__(self):
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)


def print_matrix(matrix):
    for row in range(len(matrix)):
        print(matrix[row])


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


def undirecting_matrix(dir_matrix):
    matrix = [[0 for _ in range(len(dir_matrix))] for _ in range(len(dir_matrix))]
    for i in range(len(dir_matrix)):
        for j in range(len(dir_matrix[i])):
            if dir_matrix[i][j]:
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix


def position_of_vertex(amount):
    vertex = []
    x = -350
    y = 200
    for i in range(amount):
        if i < amount / 2 - 1:
            x += DISTANCE_BETWEEN_V
            vertex.append(Vertex(x, y, i))
        elif i < amount / 2 + 1:
            y -= DISTANCE_BETWEEN_V
            vertex.append(Vertex(x, y, i))
        elif i < amount - 1:
            x -= DISTANCE_BETWEEN_V
            vertex.append(Vertex(x, y, i))
        elif i >= amount - 1:
            y += DISTANCE_BETWEEN_V
            vertex.append(Vertex(x, y, i))
    return vertex


def draw_vertex(color, vertex, num):
    turtle.setheading(0)
    turtle.color(color)
    turtle.up()
    turtle.goto(vertex[num].pos_x, vertex[num].pos_y)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(V_RADIUS)
    turtle.end_fill()
    turtle.color('white')
    turtle.write(f"{vertex[num].num + 1}", False, 'center', ('Arial', V_RADIUS, 'normal'))


def drawing_vertices(vertex):
    for i in range(len(vertex)):
        draw_vertex('blue', vertex, i)
    turtle.color('black')


def draw_loop(x, y, weight, isWeight):
    turtle.up()
    turtle.goto(x, y + V_RADIUS)
    angle = math.atan2(y - CENTER_Y, x - CENTER_X) * 180 / math.pi
    turtle.setheading(angle + 270)
    turtle.down()
    turtle.circle(25, 313)
    if isWeight:
        turtle.up()
        turtle.goto(x, y + V_RADIUS)
        angle = math.atan2(y - CENTER_Y, x - CENTER_X) * 180 / math.pi
        turtle.setheading(angle + 180)
        turtle.color('red')
        turtle.backward(40)
        turtle.down()
        turtle.write(weight, False, "center", ("Arial", 10, "normal"))
        turtle.color('black')


def draw_line(x1, y1, x2, y2):
    turtle.up()
    turtle.goto(x1, y1 + V_RADIUS)
    angle = math.atan2(y2 - y1, x2 - x1) * 180 / math.pi
    turtle.setheading(angle)
    turtle.down()
    turtle.goto(x2, y2 + V_RADIUS)


def draw_up_arc(x1, y1, x2, y2, W, isWeight):
    turtle.up()
    turtle.goto(x1, y1 + V_RADIUS)
    turtle.down()
    turtle.goto((x1 + x2)/2, y2 + ELEVATE)
    if isWeight:
        write_weight((x1 + x2)/2, y2 + ELEVATE, W)
    draw_line((x1 + x2)/2, y2 + ELEVATE - V_RADIUS, x2, y2)


def draw_down_arc(x1, y1, x2, y2, W, isWeight):
    turtle.up()
    turtle.goto(x1, y1 + V_RADIUS)
    turtle.down()
    turtle.goto((x1 + x2) / 2, y2 - ELEVATE)
    if isWeight:
        write_weight((x1 + x2) / 2, y2 - ELEVATE - 20, W)
    draw_line((x1 + x2) / 2, y2 - ELEVATE - V_RADIUS, x2, y2)


def draw_left_arc(x1, y1, x2, y2, W, isWeight):
    turtle.up()
    turtle.goto(x1, y1 + V_RADIUS)
    turtle.down()
    turtle.goto(x2 - ELEVATE, (y1 + y2) / 2 + V_RADIUS)
    if isWeight:
        write_weight(x2 - ELEVATE - 20, (y1 + y2) / 2 + V_RADIUS, W)
    draw_line(x2 - ELEVATE, (y1 + y2) / 2, x2, y2)


def draw_right_arc(x1, y1, x2, y2, W, isWeight):
    turtle.up()
    turtle.goto(x1, y1 + V_RADIUS)
    turtle.down()
    turtle.goto(x2 + ELEVATE, (y1 + y2) / 2 + V_RADIUS)
    if isWeight:
        write_weight(x2 + ELEVATE + 20, (y1 + y2) / 2 + V_RADIUS, W)
    draw_line(x2 + ELEVATE, (y1 + y2) / 2, x2, y2)


def write_weight(x, y, weight):
    turtle.up()
    turtle.goto(x, y)
    turtle.color('red')
    turtle.down()
    turtle.write(weight, False, "center", ("Arial", 10, "normal"))
    turtle.color('black')


def draw_connection_vertex(vertex, matrix, matrixW, isWeight):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if isWeight:
                condition = i <= j
            else:
                condition = True
            if matrix[i][j] and condition:
                if j == i:
                    draw_loop(vertex[i].pos_x, vertex[i].pos_y, matrixW[i][j], isWeight)
                elif vertex[i].pos_y == vertex[j].pos_y and abs(vertex[i].pos_x - vertex[j].pos_x) > DISTANCE_BETWEEN_V and (vertex[i].pos_y == UP_SIDE_Y or vertex[i].pos_y == DOWN_SIDE_Y):
                    if vertex[i].pos_y == UP_SIDE_Y:
                        draw_up_arc(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, matrixW[i][j], isWeight)
                    if vertex[i].pos_y == DOWN_SIDE_Y:
                        draw_down_arc(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, matrixW[i][j], isWeight)

                elif vertex[i].pos_x == vertex[j].pos_x and abs(vertex[i].pos_y - vertex[j].pos_y) > DISTANCE_BETWEEN_V and (vertex[i].pos_x == LEFT_SIDE_X or vertex[i].pos_x == RIGHT_SIDE_X):
                    if vertex[i].pos_x == LEFT_SIDE_X:
                        draw_left_arc(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, matrixW[i][j], isWeight)
                    elif vertex[i].pos_x == RIGHT_SIDE_X:
                        draw_right_arc(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, matrixW[i][j], isWeight)

                else:
                    draw_line(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y)
                    if isWeight:
                        turtle.backward(80)
                        turtle.color('red')
                        turtle.down()
                        turtle.write(matrixW[i][j], False, "center", ("Arial", 10, "normal"))
                        turtle.color('black')


def get_matrix_B(seed, n, k):
    matrix = create_random_matrix(seed, n)
    return multiply_matrix_on_k(matrix, k)


def get_matrix_C(undir_matrix, matrixB):
    matrix = [[0 for _ in range(len(matrixB))] for _ in range(len(matrixB))]
    for i in range(len(matrixB)):
        for j in range(len(matrixB[i])):
            matrix[i][j] = math.ceil(matrixB[i][j] * 100 * undir_matrix[i][j])
    return matrix


def get_matrix_D(matrixC):
    matrix = [[0 for _ in range(len(matrixC))] for _ in range(len(matrixC))]
    for i in range(len(matrixC)):
        for j in range(len(matrixC[i])):
            if matrixC[i][j]:
                matrix[i][j] = 1
    return matrix


def get_matrix_H(matrixD):
    matrix = [[0 for _ in range(len(matrixD))] for _ in range(len(matrixD))]
    for i in range(len(matrixD)):
        for j in range(len(matrixD[i])):
            if matrixD[i][j] != matrixD[j][i]:
                matrix[i][j] = 1
    return matrix


def get_matrix_Tr(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i < j:
                matrix[i][j] = 1
    return matrix


def get_matrix_W(matrixC, matrixD, matrixH, matrixTr):
    matrix = [[0 for _ in range(len(matrixC))] for _ in range(len(matrixC))]
    for i in range(len(matrixC)):
        for j in range(len(matrixC)):
            matrix[i][j] = (matrixD[i][j] + matrixH[i][j] * matrixTr[i][j]) * matrixC[i][j]
            matrix[j][i] = (matrixD[i][j] + matrixH[i][j] * matrixTr[i][j]) * matrixC[i][j]
    return matrix


def matrix_to_weight_graph(matrix, matrixW, vertexes):
    graphs = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                graphs.append(Edge(matrixW[i][j], vertexes[i], vertexes[j]))
    return graphs


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1


def kruskal(graphs):
    sorted_graphs = sorted(graphs, key=lambda x: x.weight)
    parent = {}
    rank = {}
    minimum_spanning_tree = List()

    for edge in sorted_graphs:
        if edge.edge_from not in parent:
            parent[edge.edge_from] = edge.edge_from
            rank[edge.edge_from] = 0
        if edge.edge_to not in parent:
            parent[edge.edge_to] = edge.edge_to
            rank[edge.edge_to] = 0

        from_root = find(parent, edge.edge_from)
        to_root = find(parent, edge.edge_to)

        if from_root != to_root:
            minimum_spanning_tree.add_edge(edge)
            union(parent, rank, from_root, to_root)

    return minimum_spanning_tree


def drawning_kruskal(graphs, vertex_pos, matrixW):
    turtle.color('orange')
    turtle.pensize(2)
    result_weight = 0
    for graph in graphs.edges:
        if graph.edge_from.num > graph.edge_to.num:
            n = graph.edge_from.num
        else:
            n = graph.edge_to.num
        result_weight += graph.weight
        matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
        matrix[graph.edge_from.num][graph.edge_to.num] = 1
        keyboard.wait('r')
        draw_connection_vertex(vertex_pos, matrix, matrixW, False)
    turtle.color('black')
    turtle.pensize(1)
    return result_weight


def main():
    n3 = 0
    n4 = 2
    n = 10
    seed = 3202
    k = 1 - n3 * 0.01 - n4 * 0.005 - 0.05
    turtle.speed(0)

    matrix = create_random_matrix(seed, n)
    matrix = multiply_matrix_on_k(matrix, k)
    direct_matrix = rounding_matrix(matrix)
    undirect_matrix = undirecting_matrix(direct_matrix)
    print('-----Undirection matrix-----')
    print_matrix(undirect_matrix)

    matrixB = get_matrix_B(seed, n, k)
    matrixC = get_matrix_C(undirect_matrix, matrixB)
    matrixD = get_matrix_D(matrixC)
    matrixH = get_matrix_H(matrixD)
    matrixTr = get_matrix_Tr(n)
    matrixW = get_matrix_W(matrixC, matrixD, matrixH, matrixTr)

    print('\n-----Weight matrix-----')
    print_matrix(matrixW)

    vertex_pos = position_of_vertex(len(undirect_matrix))

    graphs = matrix_to_weight_graph(undirect_matrix, matrixW, vertex_pos)
    draw_connection_vertex(vertex_pos, undirect_matrix, matrixW, True)
    drawing_vertices(vertex_pos)

    minimum_spanning_tree = kruskal(graphs)

    weight = drawning_kruskal(minimum_spanning_tree, vertex_pos, matrixW)
    print(f'\nResulting Weight: {weight}')
    turtle.exitonclick()


if __name__ == "__main__":
    main()
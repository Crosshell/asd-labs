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
INF = 9999


class Vertex:
    def __init__(self, pos_x, pos_y, num):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.num = num


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


def position_of_vertex(amount):
    vertex = []
    x = -350
    y = 200
    for i in range(amount):
        if i < amount / 2 - 1:
            x += DISTANCE_BETWEEN_V
            vertex.append(Vertex(x, y, i))
        elif i >= amount / 2 - 1 and i < amount / 2 + 1:
            y -= DISTANCE_BETWEEN_V
            vertex.append(Vertex(x, y, i))
        elif i >= amount / 2 + 1 and i < amount - 1:
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


def adjacency_matrix_to_graph(matrix):
    graph = {}
    num_vertices = len(matrix)
    for i in range(num_vertices):
        adjacent_vertices = []
        for j in range(num_vertices):
            if matrix[i][j] == 1:
                adjacent_vertices.append(j)
        graph[i] = adjacent_vertices
    return graph


def dfs_wrapper(matrix, vertex_pos):
    result = []
    graph = adjacency_matrix_to_graph(matrix)
    visited = {vertex: False for vertex in graph}
    tree_matrix = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    print('\nDFS Vertex list:')
    for v in range(len(graph)):
        if not visited[v]:
            list_of_vertex = [v+1]
            dfs_matrix = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
            draw_vertex('green', vertex_pos, v)
            turtle.color('red')
            result = dfs(graph, v, visited, dfs_matrix, vertex_pos, tree_matrix, list_of_vertex)
            print(result[1])
            turtle.color('black')
    print('DFS Tree Matrix:')
    print_matrix(result[0])


def dfs(graph, vertex, visited, matrix, vertex_pos, tree_matrix, list_of_vertex):
    visited[vertex] = True
    for to in graph[vertex]:
        if not visited[to]:
            turtle.setheading(0)
            keyboard.wait("r")
            matrix[vertex][to] = 1
            tree_matrix[vertex][to] = 1
            list_of_vertex.append(to+1)
            turtle.pensize(2)
            draw_connection_vertex(vertex_pos, matrix)
            turtle.pensize(1)
            draw_vertex('green', vertex_pos, vertex)
            draw_vertex('green', vertex_pos, to)
            turtle.color('red')
            matrix[vertex][to] = 0
            dfs(graph, to, visited, matrix, vertex_pos, tree_matrix, list_of_vertex)
    return tree_matrix, list_of_vertex


def bfs_wrapper(matrix, vertex_pos):
    result = []
    graph = adjacency_matrix_to_graph(matrix)
    visited = {vertex: False for vertex in graph}
    dist = {vertex: INF for vertex in graph}
    q = []
    tree_matrix = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    print('\nBFS Vertex list:')
    for v in range(len(graph)):
        if not visited[v]:
            list_of_vertex = [v + 1]
            bfs_matrix = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
            draw_vertex('green', vertex_pos, v)
            turtle.color('red')
            result = bfs(graph, v, visited, dist, q, bfs_matrix, vertex_pos, tree_matrix, list_of_vertex)
            print(result[1])
            turtle.color('black')
    print('BFS Tree Matrix:')
    print_matrix(result[0])


def bfs(graph, vertex, visited, dist, q, matrix, vertex_pos, tree_matrix, list_of_vertex):
    visited[vertex] = True
    dist[vertex] = 0
    q.append(vertex)
    while q:
        v = q.pop(0)
        for to in graph[v]:
            if not visited[to]:
                turtle.setheading(0)
                keyboard.wait("r")
                matrix[v][to] = 1
                tree_matrix[v][to] = 1
                list_of_vertex.append(to+1)
                turtle.pensize(2)
                draw_connection_vertex(vertex_pos, matrix)
                turtle.pensize(1)
                draw_vertex('green', vertex_pos, v)
                draw_vertex('green', vertex_pos, to)
                turtle.color('red')
                matrix[v][to] = 0
                visited[to] = True
                dist[to] = dist[v] + 1
                q.append(to)
    return tree_matrix, list_of_vertex


def drawing_vertices(vertex):
    for i in range(len(vertex)):
        draw_vertex('blue', vertex, i)
    turtle.color('black')


def draw_loop(x, y):
    turtle.up()
    turtle.goto(x, y + V_RADIUS)
    angle = math.atan2(y - CENTER_Y, x - CENTER_X) * 180 / math.pi
    turtle.setheading(angle + 270)
    turtle.down()
    turtle.circle(25, 313)
    turtle.stamp()


def draw_line(x1, y1, x2, y2, is_arrow):
    turtle.up()
    turtle.goto(x1, y1 + V_RADIUS)
    angle = math.atan2(y2 - y1, x2 - x1) * 180 / math.pi
    turtle.setheading(angle)
    turtle.down()
    turtle.goto(x2, y2 + V_RADIUS)
    if is_arrow:
        turtle.backward(V_RADIUS)
        turtle.stamp()


def draw_up_arc(x1, y1, x2, y2, e):
    turtle.up()
    turtle.goto(x1, y1 + V_RADIUS)
    turtle.down()
    turtle.goto((x1 + x2)/2, y2 + e)
    draw_line((x1 + x2)/2, y2 + e - V_RADIUS, x2, y2, False)


def draw_down_arc(x1, y1, x2, y2, e):
    turtle.up()
    turtle.goto(x1, y1 + V_RADIUS)
    turtle.down()
    turtle.goto((x1 + x2) / 2, y2 - e)
    draw_line((x1 + x2) / 2, y2 - e - V_RADIUS, x2, y2, False)


def draw_left_arc(x1, y1, x2, y2, e):
    turtle.up()
    turtle.goto(x1, y1 + V_RADIUS)
    turtle.down()
    turtle.goto(x2 - e, (y1 + y2) / 2 + V_RADIUS)
    draw_line(x2 - e, (y1 + y2) / 2, x2, y2, False)


def draw_right_arc(x1, y1, x2, y2, e):
    turtle.up()
    turtle.goto(x1, y1 + V_RADIUS)
    turtle.down()
    turtle.goto(x2 + e, (y1 + y2) / 2 + V_RADIUS)
    draw_line(x2 + e, (y1 + y2) / 2, x2, y2, False)


def draw_connection_vertex(vertex, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            elevate = 70
            if matrix[i][j]:
                if matrix[i][j] == matrix[j][i] and vertex[i].num > vertex[j].num:
                    elevate = elevate * 2 - 10
                if j == i:
                    draw_loop(vertex[i].pos_x, vertex[i].pos_y)
                elif vertex[i].pos_y == vertex[j].pos_y and abs(vertex[i].pos_x - vertex[j].pos_x) > DISTANCE_BETWEEN_V and (vertex[i].pos_y == UP_SIDE_Y or vertex[i].pos_y == DOWN_SIDE_Y):
                    if vertex[i].pos_y == UP_SIDE_Y:
                        draw_up_arc(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, elevate)
                    if vertex[i].pos_y == DOWN_SIDE_Y:
                        draw_down_arc(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, elevate)

                elif vertex[i].pos_x == vertex[j].pos_x and abs(vertex[i].pos_y - vertex[j].pos_y) > DISTANCE_BETWEEN_V and (vertex[i].pos_x == LEFT_SIDE_X or vertex[i].pos_x == RIGHT_SIDE_X):
                    if vertex[i].pos_x == LEFT_SIDE_X:
                        draw_left_arc(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, elevate)
                    elif vertex[i].pos_x == RIGHT_SIDE_X:
                        draw_right_arc(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, elevate)

                else:
                    if matrix[i][j] == matrix[j][i] and vertex[i].num > vertex[j].num:
                        draw_line(vertex[i].pos_x, vertex[i].pos_y, (vertex[i].pos_x + vertex[j].pos_x) / 1.87, (vertex[i].pos_y + vertex[j].pos_y) / 2 - 20, False)
                        draw_line((vertex[i].pos_x + vertex[j].pos_x) / 1.87, (vertex[i].pos_y + vertex[j].pos_y) / 2 - 20, vertex[j].pos_x, vertex[j].pos_y, True)
                    else:
                        draw_line(vertex[i].pos_x, vertex[i].pos_y, vertex[j].pos_x, vertex[j].pos_y, True)


def display_message(message, y):
    turtle.up()
    turtle.goto(-200, y)
    turtle.down()
    turtle.write(message, False, 'center', ('Arial', V_RADIUS, 'normal'))


def draw_graph(direct_matrix):
    vertex_pos = position_of_vertex(len(direct_matrix))
    draw_connection_vertex(vertex_pos, direct_matrix)
    drawing_vertices(vertex_pos)

    display_message("Direction Graph DFS, Press R to draw", y=-300)
    dfs_wrapper(direct_matrix, vertex_pos)
    display_message("Press R to BFS", y=-350)
    keyboard.wait("r")
    turtle.clear()

    vertex_pos = position_of_vertex(len(direct_matrix))
    draw_connection_vertex(vertex_pos, direct_matrix)
    drawing_vertices(vertex_pos)

    display_message("Direction Graph BFS, Press R to draw", y=-300)
    bfs_wrapper(direct_matrix, vertex_pos)


def main():
    n3 = 0
    n4 = 2
    n = 10
    seed = 3202
    k = 1 - n3 * 0.01 - n4 * 0.005 - 0.15
    turtle.speed(0)

    matrix = create_random_matrix(seed, n)
    matrix = multiply_matrix_on_k(matrix, k)
    direct_matrix = rounding_matrix(matrix)
    print('-----Direction matrix-----')
    print_matrix(direct_matrix)

    draw_graph(direct_matrix)
    turtle.exitonclick()


if __name__ == "__main__":
    main()

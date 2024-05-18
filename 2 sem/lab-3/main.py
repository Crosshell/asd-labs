import random
import turtle
import math


class Vertex:
    def __init__(self, pos_x, pos_y, num):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.num = num

def random_matrix(n): #Генерація матриці
    matrix = []
    random.seed(3202)
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(random.uniform(0, 2.0))
        matrix.append(row)
    return matrix

def change_matrix(matrix, n, k): #Змінення матриці за варіантом (напрямлена матриця)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = math.floor(matrix[i][j] * k)
    return matrix

def print_matrix(matrix): #Вивід матриці
    for i in range(len(matrix)):
        print(matrix[i])

def undirecting_matrix(matrix, n): #Перетворення напрямленої матриці на ненапрямлену
    undir_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                undir_matrix[i][j] = 1
                undir_matrix[j][i] = 1
    return undir_matrix

def position_vertex(n): #Визначення позиції вершин
    vertex = []
    x = -300
    y = 300
    for i in range(n):
        if i < n / 2 - 1:
            x += 150
            vertex.append(Vertex(x, y, i))
        if i >= n / 2 - 1 and i < n / 2 + 1:
            y -= 150
            vertex.append(Vertex(x, y, i))
        if i >= n / 2 + 1 and i < n - 1:
            x -= 150
            vertex.append(Vertex(x, y, i))
        if i >= n - 1:
            y += 150
            vertex.append(Vertex(x, y, i))
    return vertex

def drawing_vertex(vertex, n): #Малювання вершин
    turtle.setheading(0)
    for i in range(n):
        turtle.up()
        turtle.color('blue')
        turtle.goto(vertex[i].pos_x, vertex[i].pos_y - 20)
        turtle.down()
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()
        turtle.color('white')
        if i < n/2:
            turtle.write(f"{vertex[i].num+1}", False, 'center', ('Arial', 20, 'normal'))
        if i >= n/2:
            turtle.write(f"{vertex[i].num+1}", False, 'center', ('Arial', 20, 'normal'))
        turtle.color('black')


def draw_arrow(): #Малювання стрілок
    turtle.backward(20)
    turtle.color('red')
    turtle.left(150)
    turtle.forward(20)
    turtle.backward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.color('black')



def connection_vertex(vertex, matrix, isDir, n): #Малювання з'єднаннь вершин
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                if i == j:
                    x = vertex[i].pos_x
                    y = vertex[i].pos_y
                    turtle.up()
                    turtle.goto(x, y)
                    turtle.down()
                    angle = math.atan2(vertex[i].pos_y - y, vertex[i].pos_x - x) * 180 / math.pi
                    turtle.setheading(angle + 90)
                    turtle.circle(25, 310)
                    if isDir:
                        turtle.forward(20)
                        draw_arrow()
                elif ((vertex[i].pos_y == vertex[j].pos_y and abs(vertex[i].pos_x - vertex[j].pos_x) > 150)
                      or (vertex[i].pos_x == vertex[j].pos_x and abs(vertex[i].pos_y - vertex[j].pos_y) > 150)):

                    turtle.up()
                    turtle.goto(vertex[j].pos_x, vertex[j].pos_y)
                    turtle.down()

                    if vertex[i].pos_y == 300 and vertex[j].pos_y == 300:
                        if matrix[i][j] == matrix[j][i] and isDir and vertex[i].num > vertex[j].num:
                            turtle.goto((vertex[i].pos_x + vertex[j].pos_x) / 2, vertex[i].pos_y + 130)
                        else:
                            turtle.goto((vertex[i].pos_x + vertex[j].pos_x) / 2, vertex[i].pos_y+70)

                    if vertex[i].pos_y == 0 and vertex[j].pos_y == 0:
                        if matrix[i][j] == matrix[j][i] and isDir and vertex[i].num > vertex[j].num:
                            turtle.goto((vertex[i].pos_x + vertex[j].pos_x) / 2, vertex[i].pos_y - 130)
                        else:
                            turtle.goto((vertex[i].pos_x + vertex[j].pos_x) / 2, vertex[i].pos_y - 70)

                    if vertex[i].pos_x == -150 and vertex[j].pos_x == -150:
                        if matrix[i][j] == matrix[j][i] and isDir and vertex[i].num > vertex[j].num:
                            turtle.goto(vertex[i].pos_x - 130, (vertex[i].pos_y + vertex[j].pos_y) / 2)
                        else:
                            turtle.goto(vertex[i].pos_x - 70, (vertex[i].pos_y + vertex[j].pos_y) / 2)

                    if vertex[i].pos_x == 300 and vertex[j].pos_x == 300:
                        if matrix[i][j] == matrix[j][i] and isDir and vertex[i].num > vertex[j].num:
                            turtle.goto(vertex[i].pos_x + 130, (vertex[i].pos_y + vertex[j].pos_y) / 2)
                        else:
                            turtle.goto(vertex[i].pos_x + 70, (vertex[i].pos_y + vertex[j].pos_y) / 2)

                    current_position = turtle.position()
                    angle = math.atan2(vertex[i].pos_y - current_position[1], vertex[i].pos_x - current_position[0]) * 180 / math.pi
                    turtle.setheading(angle)
                    turtle.goto(vertex[i].pos_x, vertex[i].pos_y)
                    if isDir:
                        draw_arrow()

                else:
                    angle = math.atan2(vertex[i].pos_y - vertex[j].pos_y, vertex[i].pos_x - vertex[j].pos_x) * 180 / math.pi
                    turtle.setheading(angle)
                    turtle.up()
                    turtle.goto(vertex[j].pos_x, vertex[j].pos_y)
                    turtle.down()
                    if matrix[i][j] == matrix[j][i] and isDir and vertex[i].num > vertex[j].num:
                        turtle.goto((vertex[i].pos_x + vertex[j].pos_x) / 3 + 25,(vertex[i].pos_y + vertex[j].pos_y) / 2 + 10)
                        current_position = turtle.position()
                        angle = math.atan2(vertex[i].pos_y - current_position[1],vertex[i].pos_x - current_position[0]) * 180 / math.pi
                        turtle.setheading(angle)
                        turtle.goto(vertex[i].pos_x, vertex[i].pos_y)
                        draw_arrow()
                        turtle.up()

                    else:
                        turtle.goto(vertex[i].pos_x, vertex[i].pos_y)
                        if isDir:
                            draw_arrow()
                        turtle.up()


def main():
    n3 = 0
    n4 = 2
    n = 10
    k = 1 - n3 * 0.02 - n4 * 0.005 - 0.25

    direct_matrix = change_matrix(random_matrix(n), n, k)
    undirect_matrix = undirecting_matrix(direct_matrix, n)
    print('-----Direction matrix-----')
    print_matrix(direct_matrix)
    print('-----Undirection matrix-----')
    print_matrix(undirect_matrix)

    turtle.speed(0)

    isDir = int(input('Enter 0 for undirect 1 for direct:\n'))

    vertexes = position_vertex(n)

    connection_vertex(vertexes, direct_matrix, isDir, n)

    drawing_vertex(vertexes, n)

    turtle.exitonclick()


main()

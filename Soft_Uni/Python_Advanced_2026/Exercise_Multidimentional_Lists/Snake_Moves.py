from collections import deque

def snake_moves(rows, cols, snake_string):
    matrix = []
    snake = deque(snake_string)

    for row in range(rows):
        current_row = []

        for _ in range(cols):
            current_row.append(snake.popleft())
            snake.append(current_row[-1])

        if row % 2 != 0:
            current_row.reverse()

        matrix.append(current_row)
    return matrix

rows, cols = map(int, input().split())
snake_string = input()

result_matrix = snake_moves(rows, cols, snake_string)

for row in result_matrix:
    print(''.join(row))

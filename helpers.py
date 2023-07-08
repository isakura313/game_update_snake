from random import randrange, choice


# print(choice([i for i in range(0,9) if i not in [2,5,7]]))
# https://www.geeksforgeeks.org/python-split-nested-list-into-two-lists


def gameOver(row, col, gameHeight, gameWidth, snake):
    if row < 0 or row >= gameHeight or col < 0 or col >= gameWidth or snake.count([row, col]) > 1:
        return True
    return False


def applePositionInside(snake, gameHeight, gameWidth):
    x_line, y_line = map(list, zip(*snake))
    x = choice([i for i in range(0, gameHeight) if i not in x_line])
    y = choice([i for i in range(0, gameWidth) if i not in y_line])
    return [x, y]

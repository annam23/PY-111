def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    board = [[0] * (shape[1] + 2) for i in range(shape[0])]
    board[0][0] = 1
    CONST_WAY = 2

    # for row in range(len(board)):
    #     for elem in range(len(board[row])):
    #         print(board[row][elem], end=' ')

            # if board[row][elem] != 0:
            #     if row + 1 < len(board) and elem + 2 < len(board[row]):
            #         board[row + 1][elem + 2] += CONST_WAY * board[row][elem]
            #     if row + 2 < len(board) and elem + 1 < len(board[row]):
            #         board[row + 2][elem + 1] += CONST_WAY * board[row][elem]
            #     if row + 1 < len(board) and elem >= 2:
            #         board[row + 1][elem - 2] += CONST_WAY * board[row][elem]
            #     if row + 2 < len(board) and elem >= 1:
            #         board[row + 2][elem - 1] += CONST_WAY * board[row][elem]

    for row in range(len(board)):
        for elem in range(len(board[row]) - 2):
            board[row][elem] += CONST_WAY * (board[row - 1][elem + 2] + board[row - 1][elem - 2] + board[row - 2][elem + 1] + board[row - 2][elem - 1])

    return board[point[0]][point[1]]










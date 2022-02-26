def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    board = [[0] * shape[0] for i in range(shape[1])]
    board[0][0] = 1

    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            print(board[i][j], end=' ')
        print()


calculate_paths((3,6), (1,1))
Board = list[list[int]]

def day4_part1(lines: list[str]):
    numbers, boards = parse_input(lines)
    for target in numbers: 
        for board in boards:
            mark_number(board, target)
            if won(board):
                return sum_of_all_unmarked(board) * target

def day4_part2(lines: list[str]):
    numbers, boards = parse_input(lines)
    boards_copy = boards.copy()
    total = len(boards)
    
    for target in numbers:
        for i, board in enumerate(boards_copy):
            if not board: 
                continue
            
            mark_number(board, target)
            
            if won(board):
                if total == 1:
                    return sum_of_all_unmarked(board) * target
                else:
                    total -= 1
                    boards_copy[i] = None
        

def parse_input(lines: list[str]):
    org_numbers, *org_boards = lines
    numbers = list(map(int, org_numbers.strip().split(',')))

    curr: Board = []
    boards: list[Board] = []

    for i, line in enumerate(org_boards):
        if (line == '\n' and i > 0):
            boards.append(curr)
            curr = []
        elif i > 0:
            row = list(map(lambda num: int(num), list(filter(lambda x: x != '', line.strip().split(' ')))))
            curr.append(row)
        
        if i == len(org_boards) - 1 and curr:
            boards.append(curr)
    
    return numbers, boards

def won(board: Board):
    return won_vertical(board) or won_horizontal(board)

def won_vertical(board: Board):
    transposed: Board = []
    for row in range(5):
        transposed.append([0] * 5)
        for col in range(5):
            transposed[row][col] = board[col][row]

    return won_horizontal(transposed)
    

def won_horizontal(board: Board):
    return any(all(num == True for num in row) for row in board)

def mark_number(board: Board, target: int):
    for row in board: 
        for i, num in enumerate(row):
            if num == target:
                row[i] = True
    return board

def sum_of_all_unmarked(board: Board):
    flat_board = [el for row in board for el in row]
    return sum(list(filter(lambda num: type(num) is int, flat_board)))


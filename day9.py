import collections
from functools import reduce
from typing import Deque, List, Set, Tuple

def day9_part1(lines: List[str]):
    grid = [list(map(int, list(line.strip()))) for line in lines]
    
    result = 0
    
    for x, row in enumerate(grid):
        for y, digit in enumerate(row):
            if is_lowest(grid, (x, y)):
                result += digit + 1
    return result 

def day9_part2(lines: List[str]):
    grid = [list(map(int, list(line.strip()))) for line in lines]

    height, width = len(grid), len(grid[0])
    
    total_count: List[int] = []
    
    visited: Set[Tuple[int, int]] = set()

    def bfs(x: int, y: int) -> int:
        queue: Deque[Tuple[int, int]] = collections.deque()
        queue.append((x, y))
        visited.add((x, y))

        directions = [
            [0, 1], [0, -1], [1, 0], [-1, 0]
        ]

        count = 0

        while queue: 
            row, col = queue.popleft()
            count += 1
            for dr, dc in directions: 
                r, c = row + dr, col + dc

                if (r in range(height) and c in range(width)) and (r, c) not in visited and grid[r][c] != 9:
                    queue.append((r, c))
                    visited.add((r, c))

        return count


    for x, row in enumerate(grid):
        for y, digit in enumerate(row):
            if digit != 9 and (x, y) not in visited: 
                count = bfs(x, y)
                total_count.append(count)
    
    total_count = sorted(total_count, reverse=True)[:3]
    
    return reduce(lambda acc, cur: acc * cur, total_count, 1)

def is_lowest(grid: List[List[int]], pos: Tuple[int, int]):
    row, col = pos
    height, width = len(grid), len(grid[0])

    left = grid[row][col] < (grid[row][col - 1] if col - 1 in range(width) else -1)
    right = grid[row][col] < (grid[row][col + 1] if col + 1 in range(width) else 10)
    top = grid[row][col] < (grid[row - 1][col] if row - 1 in range(height) else -1)
    bottom = grid[row][col] < (grid[row + 1][col] if row + 1 in range(height) else 10)
    
    if row == 0: 
        if col == 0: 
            return right and bottom
        elif col == width: 
            return left and bottom
        else: 
            return left and right and bottom
    elif row == height: 
        if col == 0: 
            return right and top
        elif col == width: 
            return left and top
        else: 
            return left and right and top
    
    if col == 0: 
        return top and right and bottom
    elif col == width: 
        return top and left and bottom
    
    return left and right and top and bottom

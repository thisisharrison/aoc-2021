def day5_part1(lines: list[str]):
    segments = parse_input(lines)
    count: dict[str, int] = {}

    for (start, end) in segments:
        if is_overlapped(start, end):
            count_overlap(start, end, count)
    
    result = 0

    for v in count.values():
        if v >= 2:
            result += 1
    
    return result

def day5_part2(lines: list[str]):
    segments = parse_input(lines)
    count: dict[str, int] = {}

    for (start, end) in segments:
        if is_overlapped(start, end):
            count_overlap(start, end, count)
        if is_diagonal(start, end):
            count_diagonal(start, end, count)
    
    result = 0
    
    for v in count.values():
        if v >= 2:
            result += 1
    
    return result


def parse_input(lines: list[str]):
    return [parse_line(line) for line in lines]

def parse_line(line: str):    
    return list(map(parse_segment, line.split('->')))

def parse_segment(segment: str):
    return tuple(map(int, segment.strip().split(',')))

def is_overlapped(seg1: tuple[int], seg2: tuple[int]):
    x1, y1 = list(seg1)
    x2, y2 = list(seg2)
    return x1 == x2 or y1 == y2

def is_diagonal(seg1: tuple[int], seg2: tuple[int]):
    x1, y1 = list(seg1)
    x2, y2 = list(seg2)
    return abs(x1 - x2) == abs(y1 - y2)

def count_overlap(start: tuple[int, int], end: tuple[int, int], count: dict[str, int]):
    x1, y1 = start
    x2, y2 = end
    
    if x1 == x2: 
        i = y1
        is_greater = y1 < y2
        while i <= y2 if is_greater else i >= y2:
            key = f"{x1},{i}"
            count[key] = count.get(key, 0) + 1
            i += 1 if is_greater else -1
    else:
        i = x1
        is_greater = x1 < x2
        while i <= x2 if is_greater else i >= x2:
            key = f"{i},{y1}"
            count[key] = count.get(key, 0) + 1
            i += 1 if is_greater else -1

def count_diagonal(start: tuple[int, int], end: tuple[int, int], count: dict[str, int]):
    x1, y1 = start
    x2, y2 = end
    
    x_diff = x2 - x1
    y_diff = y2 - y1
    
    count[f"{x1},{y1}"] = count.get(f'{x1},{y1}', 0) + 1

    while x_diff != 0 and y_diff != 0:
        key = f"{x1 + x_diff},{y1 + y_diff}"
        count[key] = count.get(key, 0) + 1

        x_diff += 1 if x_diff < 0 else -1
        y_diff += 1 if y_diff < 0 else -1
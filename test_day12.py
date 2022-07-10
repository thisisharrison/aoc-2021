from day12 import day12_part1, day12_part2

input1 = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end',
]

input2 = [
    'dc-end',
    'HN-start',
    'start-kj',
    'dc-start',
    'dc-HN',
    'LN-dc',
    'HN-end',
    'kj-sa',
    'kj-HN',
    'kj-dc',
]

input3 = [
    'fs-end',
    'he-DX',
    'fs-he',
    'start-DX',
    'pj-DX',
    'end-zg',
    'zg-sl',
    'zg-pj',
    'pj-he',
    'RW-he',
    'fs-DX',
    'pj-RW',
    'zg-RW',
    'start-pj',
    'he-WI',
    'zg-he',
    'pj-fs',
    'start-RW',
]

file = open('puzzles/day12.txt', 'r', newline='', encoding='utf-8')

lines = file.readlines()

def test_day12_part1():
    assert day12_part1(input1) == 10
    assert day12_part1(input2) == 19
    assert day12_part1(input3) == 226
    assert day12_part1(lines) == 4754

def test_day12_part2():
    assert day12_part1(input1) == 36
    assert day12_part1(input2) == 103
    assert day12_part1(input3) == 3509
    print(day12_part2(lines))
    # assert day12_part2(lines) == ??

test_day12_part1()
test_day12_part2()

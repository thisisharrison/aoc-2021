from day4 import day4_part1, day4_part2

input = [
    '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
    '\n',
    '22 13 17 11  0',
    ' 8  2 23  4 24',
    '21  9 14 16  7',
    ' 6 10  3 18  5',
    ' 1 12 20 15 19',
    '\n',
    ' 3 15  0  2 22',
    ' 9 18 13 17  5',
    '19  8  7 25 23',
    '20 11 10 24  4',
    '14 21 16 12  6',
    '\n',
    '14 21 17 24  4',
    '10 16 15  9 19',
    '18  8 23 26 20',
    '22 11 13  6  5',
    ' 2  0 12  3  7',
]

file = open('puzzles/day4.txt', 'r', newline='', encoding='utf-8')

lines = file.readlines()

def test_day4_part1():
    assert day4_part1(input) == 4512
    assert day4_part1(lines) == 2496

def test_day4_part2():
    assert day4_part2(input) == 1924
    assert day4_part2(lines) == 25925

test_day4_part1()
test_day4_part2()
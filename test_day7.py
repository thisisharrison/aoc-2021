from day7 import day7_part1, day7_part2

input = '16,1,2,0,4,2,7,1,2,14'

file = open('puzzles/day7.txt', 'r', newline='', encoding='utf-8')

line = file.readlines()[0]

def test_day7_part1():
    assert day7_part1(input) == 37
    assert day7_part1(line) == 336131

def test_day7_part2():
    assert day7_part2(input) == 168
    assert day7_part2(line) == 92676646

test_day7_part1()
test_day7_part2()

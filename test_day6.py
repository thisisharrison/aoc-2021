from day6 import day6_part1, day6_part2

input = '3,4,3,1,2'

file = open('puzzles/day6.txt', 'r', newline='', encoding='utf-8')

line = file.readlines()[0]

def test_day6_part1():
    assert day6_part1(input) == 5934
    assert day6_part1(line) == 373378

def test_day6_part2():
    assert day6_part2(input) == 26984457539
    assert day6_part2(line) == 1682576647495

test_day6_part1()
test_day6_part2()
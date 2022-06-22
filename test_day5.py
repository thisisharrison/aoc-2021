from day5 import day5_part1, day5_part2

input = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2'
]

file = open('day5.txt', 'r', newline='', encoding='utf-8')

lines = file.readlines()

def test_day5_part1():
    '''
    .......1..
    ..1....1..
    ..1....1..
    .......1..
    .112111211
    ..........
    ..........
    ..........
    ..........
    222111....

    count occurrences larger than 2
    '''
    assert day5_part1(input) == 5
    assert day5_part1(lines) == 5092

def test_day5_part2():
    '''
    1.1....11.
    .111...2..
    ..2.1.111.
    ...1.2.2..
    .112313211
    ...1.2....
    ..1...1...
    .1.....1..
    1.......1.
    222111....
    
    count occurrences larger than2
    '''
    assert day5_part2(input) == 12
    assert day5_part2(lines) == 20484

test_day5_part1()
test_day5_part2()
from day10 import day10_part1, day10_part2

input = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]',
]

file = open('puzzles/day10.txt', 'r', newline='', encoding='utf-8')

lines = file.readlines()

def test_day10_part1():
    assert day10_part1(input) == 26397
    assert day10_part1(lines) == 216297

def test_day10_part2():
    assert day10_part2(input) == 288957
    assert day10_part2(lines) == 2165057169

test_day10_part1()
test_day10_part2()

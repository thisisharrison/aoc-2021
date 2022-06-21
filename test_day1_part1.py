from day1 import day1_part1

def test_part1():
    input = ['199',
    '200',
    '208',
    '210',
    '200',
    '207',
    '240',
    '269',
    '260',
    '263']

    assert day1_part1(input) == 7

    with open('day1.txt', 'r', newline='', encoding='utf-8') as f:
        lines = f.readlines()
        count = day1_part1(lines) 
        assert count == 1233

test_part1()
from day1 import day1_part2

def test_part2(): 
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
    
    assert day1_part2(input) == 5

    with open('day1.txt', 'r', newline='', encoding='utf-8') as f:
        lines = f.readlines()
        count = day1_part2(lines) 
        assert count == 1275

test_part2()
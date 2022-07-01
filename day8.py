from typing import Dict, List

EASY_NUMBERS: Dict[int, int] = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

def day8_part1(lines: List[str]):
    data = list(map(lambda x: x.strip().split(' '), [line.strip().split('|')[1] for line in lines]))

    count = 0

    for row in data: 
        for digit in row: 
            if len(digit) in EASY_NUMBERS:
                count += 1

    return count

def day8_part2(lines: List[str]):
    '''
    Use signal to parse the Easy Numbers first (1, 4, 7, 8).
    Then based on the segment count: 
        count = 5 (2, 3, 5)
            - use 4 => 2 and 4 have 2 intersections
                    => 5 and 4 have 3 intersections but 5 and 1 only have 1 intersection
            - use 1 => 3 and 1 have 2 intersections. 

        count = 6 (0, 6, 9)
            - to find 0: set intersection of 2, 3, 4, 5 will separate 0 from 6 and 9. it returns the middle segment which 6 and 9 do not have 
            - use 1 => 9 and 1 have 2 intersections
                    => 6 and 1 have 1 intersection
    '''
    
    data = [line.strip().split('|') for line in lines]
    
    data_map = [
        {
            'signal': parse_signal(signal), 
            'output': parse_output(output)
        } for signal, output in data
    ]

    result = 0

    for line in data_map:
        digit_map: Dict[int, str] = {}
        signal, output = line['signal'], line['output']

        for digit in signal:
            if d := get_easy_number(digit):
                digit_map[d] = digit
            
            elif len(digit) == 5:
                decode_length_5(digit, digit_map)
            
            elif len(digit) == 6:
                decode_length_6(digit, digit_map)
        
        reversed_map = {v: k for k, v in digit_map.items()}

        result += int(''.join([str(reversed_map[x]) for x in output]))
    
    return result

def parse_signal(signal: str):
    '''
    Sort by 3 sections: Easy Numbers, Length of 5, Length of 6
    '''
    partial_parsed = parse_output(signal)
    
    def sort_criteria(digit: str):
        if len(digit) in EASY_NUMBERS:
            return 0
        elif len(digit) == 5: 
            return 1
        elif len(digit) == 6:
            return 2
    
    sorted_signal = sorted(list(map(lambda x: (x, sort_criteria(x)), partial_parsed)), key=lambda x: x[1])
    
    return list(map(lambda x: x[0], sorted_signal))


def parse_output(output: str):
    return list(map(lambda s: ''.join(sorted(s)), output.strip().split(' ')))

def get_easy_number(string: str): 
    if len(string) in EASY_NUMBERS: 
        return EASY_NUMBERS[len(string)]
    else: 
        return False

def decode_length_5(digit: str, digit_map: Dict[int, str]):
    one = digit_map.get(1, '')
    four = digit_map.get(4, '')
    
    intersections_with_one = count_intersections(digit, one)
    intersections_with_four = count_intersections(digit, four)

    if intersections_with_four == 2:
        digit_map[2] = digit
    elif intersections_with_four == 3 and intersections_with_one != 2:
        digit_map[5] = digit
    if intersections_with_one == 2: 
        digit_map[3] = digit
    

def count_intersections(s1: str, s2: str):
    return len((set(s1) & set(s2)))

def decode_length_6(digit: str, digit_map: Dict[int, str]):
    if is_zero(digit, digit_map):
        digit_map[0] = digit
    else:
        count = count_intersections(digit_map.get(1, ''), digit)
        if count == 1: 
            digit_map[6] = digit
        else:
            digit_map[9] = digit

def is_zero(digit: str, digit_map: Dict[int, str]):
    two = set(digit_map.get(2, ''))
    three = set(digit_map.get(3, ''))
    four = set(digit_map.get(4, ''))
    five = set(digit_map.get(5, ''))
    
    mid_segment = (two & three & four & five).pop()

    return mid_segment not in digit
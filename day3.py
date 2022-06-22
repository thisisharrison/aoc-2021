from enum import Enum
from functools import reduce

def day3_part1(lines: list[str]):
    acc = reduce(aggregate_bit, lines, [0] * len(lines[0].strip()))
    half = len(lines) / 2
    gamma = ['1' if x > half else '0' for x in acc]
    epsilon = ['1' if x < half else '0' for x in acc]
    return int(''.join(gamma), base=2) * int(''.join(epsilon), base=2)

def aggregate_bit(acc: list[int], cur: str):
    cur_list = list(map(int, list(cur.strip())))
    for i, num in enumerate(cur_list):
        acc[i] += num
    return acc

class Rating(Enum):
    OXYGEN = 'oxygen'
    CO2 = 'co2'

def day3_part2(lines: list[str]):
    clean_lines = list(map(lambda line: list(map(int, list(line.strip()))), lines))
    bit_length = len(clean_lines[0])

    oxygen = get_rating(Rating.OXYGEN, bit_length, clean_lines)
    co2 = get_rating(Rating.CO2, bit_length, clean_lines)
    
    return oxygen * co2

def get_rating(type: Rating, bit_length: int, lines: list[list[int]]):
    result = [''] * bit_length
    is_oxygen = type == Rating.OXYGEN

    for i in range(bit_length):
        if len(lines) == 1:
            result = list(map(str, lines[0]))
            break
        
        zero_bit_count = sum([1 if line[i] == 0 else 0 for line in lines])
        one_bit_count = sum([1 if line[i] == 1 else 0 for line in lines])

        if one_bit_count >= zero_bit_count:
            result[i] = '1' if is_oxygen else '0'
            lines = list(filter(lambda x: x[i] == (1 if is_oxygen else 0), lines))
        else: 
            result[i] = '0' if is_oxygen else '1'
            lines = list(filter(lambda x: x[i] == (0 if is_oxygen else 1), lines))

    return int(''.join(result), base=2)
import sys


def day7_part1(line: str):
    crabs = list(map(int, line.strip().split(',')))
    crabs.sort()

    mid = len(crabs) // 2
    median = crabs[mid]

    total_fuel = 0
    for crab in crabs:
        total_fuel += abs(crab - median)
    
    return total_fuel

def sum_sequence(x): 
    return ((1 + x) * x) // 2

def day7_part2(line: str):
    crabs = list(map(int, line.strip().split(',')))
    
    memo: dict[int, int] = {}
    i = min(crabs)
    least_fuel = sys.maxsize
    
    while True:
        total_fuel = 0
        for crab in crabs:
            distance = abs(crab - i) 
            fuel = memo.setdefault(distance, sum_sequence(distance))
            total_fuel += fuel

        if total_fuel < least_fuel: 
            least_fuel = total_fuel
            i += 1
        else:
            return least_fuel
    
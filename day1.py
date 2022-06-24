from typing import List


def day1_part1(lines: List[str]):
    count = 0
    for i, line in enumerate(lines): 
        curr = int(line.strip())
        if i > 0:
            prev = int(lines[i - 1].strip())
            if curr - prev > 0:
                count += 1
    return count

def day1_part2(lines: List[str]):
    l = 0
    runningSum = 0
    prevSum = 0
    count = 0

    for r in range(len(lines)):
        left = int(lines[l].strip())
        right = int(lines[r].strip())

        runningSum += right

        if r - l + 1 == 3:
            if l > 0:
                if runningSum - prevSum > 0:
                    count += 1
            prevSum = runningSum
            runningSum -= left
            l += 1

    return count

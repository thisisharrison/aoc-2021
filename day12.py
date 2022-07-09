
from collections import defaultdict
from typing import List

def day12_part1(lines: List[str]):
    graph = defaultdict(set)
    for line in lines:
        src, dest = line.strip().split('-') 
        graph[src].add(dest)
        graph[dest].add(src)
    
    print(graph)

def day12_part2(lines: List[str]):
    pass
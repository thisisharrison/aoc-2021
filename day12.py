
from collections import defaultdict
from typing import List

def day12_part1(lines: List[str]):
    graph = defaultdict(set)
    for line in lines:
        src, dest = line.strip().split('-') 
        graph[src].add(dest)
        graph[dest].add(src)

    def dfs(graph, node):
        def dfs_util(graph, node, count=0, visited=set()):
            # total count plus this path reached the end
            if node == 'end': 
                return count + 1

            if node.islower():
                # create new visited set for each possible paths
                visited = set(visited)
                visited.add(node)
            
            for child in graph[node]:
                if child not in visited:
                    # get all the path counts
                    count = dfs_util(graph, child, count, visited)
            return count
        
        return dfs_util(graph, node)

    return dfs(graph, 'start')

def day12_part2(lines: List[str]):
    pass
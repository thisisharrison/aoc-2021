from functools import reduce

def day6_part1(line: str):
    fishes = list(map(int, line.strip().split(',')))
    day = 1

    while day <= 80:
        new_fish = []
        for i, fish in enumerate(fishes):
            if fish == 0:
                fishes[i] = 6
                new_fish.append(8)
            else:
                fishes[i] = fish - 1

        fishes += new_fish
        day += 1
        new_fish.clear()
    
    return len(fishes)

def day6_part2(line: str):
    fishes = list(map(int, line.strip().split(',')))

    initial_map = {i: 0 for i in range(9)}

    def count_fish(acc, cur): 
        acc[cur] += 1
        return acc
    
    fish_map = reduce(count_fish, fishes, initial_map)

    day = 1

    while day <= 256:
        new_fish = 0
        for i in range(9):
            if i > 0: 
                fish_map[i - 1] = fish_map[i]
            else:
                new_fish = fish_map[0]
                fish_map[0] = 0
        fish_map[6] += new_fish 
        fish_map[8] = new_fish 

        day += 1
    
    return sum(fish_map.values())
    
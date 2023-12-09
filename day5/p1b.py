from itertools import batched
from functools import reduce

maps = {}
def ranger(Dstart,Sstart, incr):
    return {(Sstart,Sstart+incr):(Dstart, Dstart + incr)}



def build_map(data):
    maps = {}
    itter = iter(data)
    seeds = map(int, next(itter).split(':')[1].split())
    seeds = [s for s in batched(seeds,2)]
    next(itter, None)

    line = next(itter,None)
    while line is not None:
        l = line.split(':')[0]
        nl = next(itter)
        array = []

        while nl and nl.strip():
            Dstart, Sstart, incr = map(int, nl.split())
            array.append([Dstart, Sstart, incr])
            nl = next(itter, None)

        maps[l] = array
        line = next(itter, None)
    return seeds, maps

def traverse_map(seed):
    global maps
    next_value = []
    for _,V in maps.items():
        while len(seeds) > 0:
            s, e = seeds.pop()
            for a, b, c in V:
                os = max(s, b)
                oe = min(e, b + c)
                if os < oe:
                    next_value.append((os - b + a, oe - b + a))
                    if os > s:
                        seeds.append((s, os))
                    if e > oe:
                        seeds.append((oe, e))
                    break
            else:
                next_value.append((s, e))
        seed = next_value
           
    return seed



if __name__ == '__main__':
    data = open("/Users/ddak/work/Advent-of-Code-2023/day5/input.txt", encoding="UTF-8").read().split('\n')
    seeds, maps = build_map(data)
    locations = traverse_map(seeds)
    # Use reduce to find min of locations
    print(min(locations)[0])
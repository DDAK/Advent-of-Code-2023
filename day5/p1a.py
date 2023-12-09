# import numpy as np

# def ranger(Dstart, Sstart, incr):
#     return dict(zip(np.arange(Sstart, Sstart + incr), np.arange(Dstart, Dstart + incr)))


# def ranger(Dstart,Sstart, incr):
#     return {a: b for a, b in zip(range(Sstart, Sstart + incr), range(Dstart, Dstart + incr))}

def ranger(Dstart,Sstart, incr):
    return {(Sstart,Sstart+incr):(Dstart, Dstart + incr)}



def build_map(data):
    maps = {}
    itter = iter(data)
    seeds = next(itter).split(':')[1].split()
    next(itter, None)
    # next(itter, None)
    loc_iter = []

    line = next(itter,None)
    while line is not None:
        l = line.split(':')[0]
        nl = next(itter)
        array = {}

        while nl and nl.strip():
            Dstart, Sstart, incr = map(int, nl.split())
            array.update(ranger(Dstart, Sstart, incr))
            nl = next(itter, None)

        maps[l] = array
        loc_iter.append(l)
        line = next(itter, None)
    return seeds, loc_iter, maps

def traverse_map(seed, locs, maps):
    next_value = int(seed)
    for v in locs:
        next_value = maps[v].get(next_value,next_value)
    return next_value

if __name__ == '__main__':
    data = open("/Users/ddak/work/Advent-of-Code-2023/day5/input1.txt", encoding="UTF-8").read().split('\n')
    seeds, locs, maps = build_map(data)
    locations = [traverse_map(seed, locs, maps) for seed in seeds]

    print(min(locations))
                            
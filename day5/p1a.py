
def ranger(Dstart,Sstart, incr, Map = {}):
    for a,b in zip(range(Sstart, Sstart+incr), range(Dstart, Dstart+incr)):
        Map[a] = b

def build_map(data):
    maps = {}
    itter = data.__iter__()
    line = next(itter)
    seeds = line.split(':')[1].split()
    line = next(itter, None)
    line = next(itter, None)
    loc_iter = []
    while(line is not None):
        l = line.split(':')[0]
        nl = next(itter)
        array = {}
        while(nl is not None):
            Dstart, Sstart, incr = nl.split()
            maps[l] = ranger(int(Dstart), int(Sstart), int(incr), array)
            nl = next(itter, None)
            if nl == '':
                nl = None
        maps[l] = array
        loc_iter.append(l)
        line = next(itter, None)
    return maps, seeds, loc_iter

def traverse_map(seed, maps, locs):
    next_value = int(seed)
    for v in locs:
        next_value = maps[v].get(next_value,next_value)
    return next_value

if __name__ == '__main__':
    data = open("/Users/ddak/work/Advent-of-Code-2023/day5/input.txt", encoding="UTF-8").read().split('\n')
    maps, seeds, locs = build_map(data)
    locations = []
    for seed in seeds:
        locations.append(traverse_map(seed, maps, locs))
   
    print(min(locations))
                            
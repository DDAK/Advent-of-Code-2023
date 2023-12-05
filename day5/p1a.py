
def ranger(Dstart,Sstart, incr, Map = {}):
    for a,b in zip(range(Sstart, Sstart+incr), range(Dstart, Dstart+incr)):
        Map[a] = b


if __name__ == '__main__':
    data = open("/Users/ddak/work/Advent-of-Code-2023/day5/input1.txt", encoding="UTF-8").read().split('\n')
    maps = {}
    itter = data.__iter__()
    line = next(itter)
    seeds = line.split(':')[1].split()
    eof = 0
    line = next(itter, None)
    while(line):
        l = line.split(':')[0]
        nl = next(itter)
        array = {}
        while(nl):
            Dstart, Sstart, incr = nl.split()
            maps[l] = ranger(int(Dstart), int(Sstart), int(incr), array)
            nl = next(itter, None)
        maps[l] = array
        line = next(itter, None)
                            
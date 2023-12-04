from cProfile import Profile
from pstats import SortKey, Stats
import re
from collections import Counter


if __name__ == '__main__':
    regex = r"Card.*(?P<cardno>\d+):\s+(?P<cscores>.*)"
    cards = []
    pscards = Counter()
    with Profile() as profile:
        with open("/Users/ddak/work/Advent-of-Code-2023/day4/input.txt", encoding="UTF-8") as f:
            for card in f:
                matches = re.finditer(regex, card)
                for match in matches:
                    card_num = int(match.group("cardno"))
                    scores = match.group("cscores").split('|')
                    cscores = scores[0]
                    gscores = scores[1]
                    cs = set(cscores.split())
                    gs = set(gscores.split())
                    common = len(set.intersection(cs,gs))
                    pscards[f'card_{card_num}']+=1
                    if common != 0:
                        for c in range(0,pscards.get(f'card_{card_num}',0)):
                            for ix in range(card_num+1,card_num+1+common):
                                pscards[f'card_{ix}']+=1
            print(sum(pscards.values()))
        (
            Stats(profile)
            .strip_dirs()
            .sort_stats(SortKey.CALLS)
            .print_stats()
        )

                            
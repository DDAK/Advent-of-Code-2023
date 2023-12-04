import re
from collections import Counter


if __name__ == '__main__':
    regex = r"Card.*(?P<cardno>\d+):\s+(?P<cscores>.*)"
    cards = []
    pscards = Counter()
    data = open("/Users/ddak/work/Advent-of-Code-2023/day4/input.txt", encoding="UTF-8").read().split('\n')
    for idx, card in enumerate(data):
        card_num = idx+1
        cs = set(card.split("|")[0].split(":")[1].split())
        gs = set(card.split("|")[1].split())
        common = len(set.intersection(cs,gs))
        pscards[f'card_{card_num}']+=1
        for _ in range(0,pscards.get(f'card_{card_num}')):
            for ix in range(card_num+1,card_num+1+common):
                pscards[f'card_{ix}']+=1
    print(sum(pscards.values()))
#1144152497
                            
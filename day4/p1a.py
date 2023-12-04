import re

if __name__ == '__main__':
    regex = r"Card.*(?P<cardno>\d+):\s+(?P<cscores>.*)"
    cards = []
    with open("/Users/ddak/work/Advent-of-Code-2023/day4/input.txt", encoding="UTF-8") as f:
        for card_num, card in enumerate(f):
            matches = re.finditer(regex, card)
            for match in matches:
                _ = match.group("cardno")
                scores = match.group("cscores").split('|')
                cscores = scores[0]
                gscores = scores[1]
                cs = set(cscores.split())
                gs = set(gscores.split())
                common = len(set.intersection(cs,gs))
                if common != 0:
                    cards.append(pow(2,common-1))
        print(sum(cards))

                            
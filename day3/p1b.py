import re
r = '[0-9]+'
def scan(dir, lines,lno, chno):
    nums = []
    if dir in ['L', 'R']:
        matches = re.finditer(r, lines[lno])
        for match in matches:
            span = match.span()
            num = match.group()
            if chno == span[0]-1 or span[1]==chno:
                nums.append(num)
    elif dir in ['TL','T','TR']:
        matches = re.finditer(r, lines[lno-1])
        for match in matches:
            span = match.span()
            num = match.group()
            if chno == span[0]-1 or span[1]==chno or (chno >=span[0] and chno < span[1]):
                nums.append(num)
    elif dir in ['BL', 'B', 'BR']:
        matches = re.finditer(r, lines[lno+1])
        for match in matches:
            span = match.span()
            num = match.group()
            if chno == span[0]-1 or span[1]==chno or (chno >=span[0] and chno < span[1]):
                nums.append(num)
    return nums
if __name__ == '__main__':
    gear = []
    lines = []
    directions = ['L', 'T', 'B']
    with open("input.txt", encoding="UTF-8") as f:
        for line in f:
            lines.append(line)            
    for lno,line in enumerate(lines):
        for chno, char in enumerate(line):
            sch = []       
            if char not in '0123456789.\n':
                for dir in directions:
                  n = scan(dir,lines,lno,chno)
                  if n is not []:
                    for a in n:
                        sch.append(a)
                if len(sch)==2:
                    gear.append(int(sch[0])*int(sch[1]))
    print(sum(gear))

                            
import re
if __name__ == '__main__':
    sum = 0
    num_name = {"one":1,
            "two":2, 
            "three":3, 
            "four":4, 
            "five":5, 
            "six":6, 
            "seven":7, 
            "eight":8, 
            "nine":9}
    r = '1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'
    num = list()
    with open("input.txt", encoding="UTF-8") as f:            
        for line in f:
            matches = re.findall(rf'(?=({r}))', line)
            for idx, val in  enumerate(matches):
                if  val in num_name.keys():
                    matches[idx]= str(num_name[val])
            print(line, num, matches)
            sum += int(matches[0]+matches[-1])
    print(sum)


if __name__ == '__main__':
    sum = 0
    with open("input.txt") as f:
        for line in f:
             numbers = [ c for c in line if c.isdigit()]
             sum += int(numbers[0]+numbers[-1])
    print(sum)


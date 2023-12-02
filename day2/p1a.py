import re
if __name__ == '__main__':
    possible_colors = {'red':12, 'green':13, 'blue':14}
    regex = r"Game (?P<game_number>\d+):\s+(?P<scores>.*)"
    game_data = {}
    with open("input.txt", encoding="UTF-8") as f:            
        for line in f:
            matches = re.finditer(regex, line)

            for match in matches:
                game_number = match.group("game_number")
                scores = match.group("scores")

                # Split scores into individual rounds
                rounds = scores.split(";")

                # Process each round
                round_dict = {}
                for round_num, round in enumerate(rounds):
                    round_data = re.findall(r"(\d+)\s+(\w+)", round)
                    round_dict[round_num] = {color: int(count) for count, color in round_data}
                game_data[game_number]  = round_dict
        possible_games = []
        for game, rounds in game_data.items():
            possible = 0
            for round, colors in rounds.items():
                for k, v in colors.items():
                    if colors[k] > possible_colors[k]:
                        possible = 1
                        break
                if possible == 1:
                    break
            if possible == 0:
                possible_games.append(game)
        print(possible_games)
        print(sum([ int(g) for g in possible_games]))

import re
if __name__ == '__main__':
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
        game_power = []
        for game, rounds in game_data.items():
            possible = 0
            max_game_colors = {'red':-1, 'green':-1, 'blue':-1}
            for round, colors in rounds.items():
                for k, v in colors.items():
                    if colors[k] > max_game_colors[k]:
                        max_game_colors[k] = colors[k]
            game_power.append(max_game_colors['red']*max_game_colors['blue']*max_game_colors['green'])
        print(sum(game_power))

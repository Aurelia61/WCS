from game import game

games =[]

# add game with constructor
games.append(game("player_1", "racing", "features_1"))
games.append(game("player_2", "board_2", "features_2"))

# print all games
for current_game in games :
    print(f'le {current_game.player} joue sur le plateau {current_game.board} en respectant les régles {current_game.features}.')


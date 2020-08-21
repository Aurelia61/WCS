# from models.game import Game

# games =[]

# # add game with constructor
# games.append(Game("player_1", "racing", "features_1"))
# games.append(Game("player_2", "board_2", "features_2"))

# # print all games
# for current_game in games :
#     print(f'le {current_game.player} joue sur le plateau {current_game.board} en respectant les régles {current_game.features}.')



# coding: utf-8

#imports
import variables
import models.player as Player
import models.part as Player


# functions
def main():
    """
        Main entry
    """

    # add players to collection
    variables.players.append(Player("Guillaume", "\033[34m"))
    variables.players.append(Player("Alex", "\033[31m"))
    print()

    #add parts to players
    for my_player in variables.players:
        my_player.parts.append(Part("Tour", "T", 1,1))
        my_player.parts.append(Part("Cavalier", "C", 1,2))


    # print players with parts
    for my_player in variables.players:
        for my_part in my_player.parts:
            print (my_part.name)


if __name__ == "__main__":
    main()
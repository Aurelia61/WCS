# coding: utf-8

class Game():
    """
        generic class to manage a game //Game model
    """

    # global (static) properties                  !!! me rappelle plus ce que c'est :-( --- Est-ce indispensable ??

    # methods

    def __init__(self, player, board, features) :       # !!! Est-on obligé de mettre des valeurs par défaut dans init ???
                                                        #  et de mettre TOUTES les propriétés ??????????????
        """
            Game constructor
        """

        # instance properties
        self.player = player
        self.board = board
        self.features = features

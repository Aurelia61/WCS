# coding: utf-8

class board():
    """
        generic class to manage a board
    """

    # global (static) properties

    # methods

    def __init__(self, size, color) :
        """
            board constructor
        """

        # instance properties
        self.size = size
        self.color = color       # est-ce qu'on peut utiliser la même classe que pour la couleur des joueurs ????

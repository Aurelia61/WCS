# coding: utf-8

class Player():
    """
        generic class to manage a player // Player model
    """

    # global (static) properties

    # methods

    def __init__(self, color, name) :
        """
            Player constructor
        """

        # instance properties
        self.color = color
        self.name = name
        self.part = []

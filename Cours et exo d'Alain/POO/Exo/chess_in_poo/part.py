# coding: utf-8

class part():
    """
        generic class to manage a part
    """

    # global (static) properties

    # methods

    def __init__(self, name, symbol, pos_x, pos_y) :
        """
            part constructor
        """

        # instance properties
        self.name = name
        self.symbol = symbol
        self.pos_x = pos_x
        self.pos_y = pos_y
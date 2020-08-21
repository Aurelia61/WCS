# coding: utf-8

class Part():
    """
        generic class to manage a part // Part model
    """

    # global (static) properties

    # methods

    def __init__(self, name, symbol, pos_x, pos_y) :
        """
            Part constructor
        """

        # instance properties
        super().__init__()       # appelle le constructeur de la classe supérieuredont cette classe hérite
        
        self.name = name
        self.symbol = symbol
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.movements = None
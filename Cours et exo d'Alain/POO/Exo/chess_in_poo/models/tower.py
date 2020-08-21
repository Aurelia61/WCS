

class Tower(part):       # car hérite de la classe Part
    """
        tower chess part model
    """

def __init__(self, pos_x, pos_y) :
        """
            Part constructor
        """

        # instance properties

        movement_x = "n"    # bouge de n cases en x
        movement_y = "n"    # bouge de n cases en y
        
        super().__init__("Tower", "T", pos_x, pos_y)       # appelle le constructeur de la classe supérieure dont cette classe hérite
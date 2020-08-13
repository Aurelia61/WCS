# coding: utf-8

class feature():
    """
        generic class to manage a feature
    """

    # global (static) properties

    # methods

    def __init__(self, nb_player, games_rules, age_to_play, average_play_time, parts_list) :
        """
            feature constructor
        """

        # instance properties
        self.nb_player = nb_player
        self.games_rules = games_rules
        self.age_to_play = age_to_play
        self.average_play_time = average_play_time
        self.parts_list = parts_list            # est-ce qu'on peut aller chercher les données dans la classe "part" ??????????
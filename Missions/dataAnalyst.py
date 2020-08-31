import random

class dataAnalyst():
    """
        Generic class for data analyst
    """

    def __init__(self, 
        Name = "", 
        FirstName = "", 
        Age = 0, 
        Sex = "",
        formationPrecedente = "",
        motivation = 100,
        progression = 0):
        """
            data analyst constructor
        """

        self.Name = Name
        self.FirstName = FirstName
        self.Age = Age
        self.Sex = Sex
        self.formationPrecedente = formationPrecedente
        self.motivation = 100
        self.progression = 0


    def suivreFormation(self):
        """
            chaque fois qu'elle est utilisée, 
            cette méthode diminue la motivation d'une valeur entière aléatoire (random) entre 5 et 25 
            et augmente la progression d'une valeur entière aléatoire entre 20 et 30
        """
        motivationRandom = random.randint(5,25)
        self.motivation -= motivationRandom
        progressionRandom = random.randint(20,30)
        self.progression += progressionRandom

    def bosserPlus(self):
        """
            chaque fois qu'elle est utilisée, 
            cette méthode augmente la motivation et la progression 
            d'une valeur entière aléatoire entre 10 et 30
        """
        numRandom = random.randint(10,30)
        self.motivation += numRandom
        self.progression += numRandom

    def echouer(self):
        """
            chaque fois qu'elle est utilisée 
            baisse la motivation d'une valeur entre 20 et 40 et 
            augmente la progression d'une valeur entre 20 et 40
        """
        motivEchouerRandom = random.randint(20,40)
        self.motivation -= motivEchouerRandom
        progrEchouerRandom = random.randint(20,40)
        self.progression += progrEchouerRandom

    def reussir(self):
        """
            chaque fois qu'elle est utilisée, 
            augmente la motivation d'une valeur entre 20 et 40 et 
            augmente la progression d'une valeur random entre 10 et 20
        """
        motivReussierRandom = random.randint(20,40)
        self.motivation += motivReussierRandom
        progrReussirRandom = random.randint(10,20)
        self.progression += progrReussirRandom



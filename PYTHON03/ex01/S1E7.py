from S1E9 import Character


class Baratheon(Character):
    """Classe représentant un membre de la famille Baratheon."""

    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"
    __doc__ = "Classe représentant un membre de la famille Baratheon."

    def __init__(self, first_name, is_alive=True):
        """
        Initialise un Baratheon.
        first_name (str): Le prénom du personnage.
        is_alive (bool, optional): True si le personnage est vivant.
        Par défaut True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = Baratheon.family_name
        self.eyes = Baratheon.eyes
        self.hairs = Baratheon.hairs

    def __str__(self):
        """
        Retourne une représentation textuelle du Baratheon.
        """
        txt = f"Baratheon: {self.family_name}, "
        txt += f"Eyes: {self.eyes}, "
        txt += f"Hairs: {self.hairs}"
        return (txt)

    def __repr__(self):
        """
        Retourne une représentation textuelle lisible du Baratheon.
        """
        return self.__str__()

    def die(self):
        """
        Fait mourir le Baratheon.
        """
        super().die()


class Lannister(Character):
    """Classe représentant un membre de la famille Lannister."""

    family_name = "Lannister"
    eyes = "blue"
    hairs = "light"
    __doc__ = "Classe représentant un membre de la famille Lannister."

    def __init__(self, first_name, is_alive=True):
        """
        Initialise un Lannister.
        first_name (str): Le prénom du personnage.
        is_alive (bool, optional): True si le personnage est vivant.
        Par défaut True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = Lannister.family_name
        self.eyes = Lannister.eyes
        self.hairs = Lannister.hairs

    def __str__(self):
        """
        Retourne une représentation textuelle du Lannister.
        """
        txt = f"Lannister: {self.first_name}, "
        txt += f"Eyes: {self.eyes}, "
        txt += f"Hairs: {self.hairs}"
        return (txt)

    def __repr__(self):
        """
        Retourne une représentation textuelle lisible du Lannister.
        """
        return self.__str__()

    def die(self):
        """
        Fait mourir le Lannister.
        """
        self.is_alive = False

    @staticmethod
    def create_lannister(first_name, is_alive=True):
        """
        Crée une nouvelle instance de Lannister.
        first_name (str): Le prénom du personnage.
        is_alive (bool, optional): True si le personnage est vivant.
        Par défaut True.
        """
        return __class__(first_name, is_alive)

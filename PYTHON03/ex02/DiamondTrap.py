from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Représente un roi héritant des maisons Baratheon et Lannister.
    Attributs :
        first_name (str): Le prénom du roi.
        is_alive (bool): Indique si le roi est en vie (par défaut True).
        eyes (str): Couleur des yeux du roi.
        hairs (str): Couleur des cheveux du roi.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initialise un roi avec un prénom et un état de vie.
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        """
        Définit la couleur des yeux du roi.
        """
        self.eyes = eyes

    def set_hairs(self, hairs):
        """
        Définit la couleur des cheveux du roi.
        """
        self.hairs = hairs

    def get_eyes(self):
        """
        Retourne la couleur des yeux du roi.
        """
        return self.eyes

    def get_hairs(self):
        """
        Retourne la couleur des cheveux du roi.
        """
        return self.hairs

    def __str__(self):
        """
        Retourne une représentation textuelle du roi.
        """
        return super().__str__(self)

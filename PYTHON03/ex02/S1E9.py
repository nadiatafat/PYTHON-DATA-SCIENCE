from abc import ABC, abstractmethod


class Character(ABC):
    """Classe abstraite représentant un personnage de Game of Thrones."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialise un personnage.
        first_name (str): Le prénom du personnage.
        is_alive (bool, optional): True si le personnage est vivant.
        Par défaut True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Méthode abstraite qui doit faire mourir le personnage."""
        self.is_alive = False


class Stark(Character):
    """Classe représentant un membre de la famille Stark."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialise un Stark.
        first_name (str): Le prénom du personnage.
        is_alive (bool, optional): True si le personnage est vivant.
        Par défaut True.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """Fait mourir le Stark."""
        super().die()

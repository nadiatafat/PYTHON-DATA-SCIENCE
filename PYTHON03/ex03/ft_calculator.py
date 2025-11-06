class calculator:
    """
    Une classe représentant un vecteur numérique et permettant
    d'effectuer des opérations mathématiques avec un scalaire :
      - Addition : v + 5
      - Soustraction : v - 5
      - Multiplication : v * 5
      - Division : v / 5

    Attributs :
        vector (list[float]) : Le vecteur stocké dans l'objet calculator.
    """

    def __init__(self, vector: list[float]):
        """Initialise le vecteur interne de la calculatrice."""
        self.vector = vector

    def __add__(self, scalar: float) -> None:
        """Additionne un scalaire à chaque élément du vecteur."""
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)

    def __sub__(self, scalar: float) -> None:
        """Soustrait un scalaire à chaque élément du vecteur."""
        self.vector = ([x - scalar for x in self.vector])
        print(self.vector)

    def __mul__(self, scalar: float) -> None:
        """Multiplie chaque élément du vecteur par un scalaire."""
        self.vector = ([x * scalar for x in self.vector])
        print(self.vector)

    def __truediv__(self, scalar: float) -> None:
        """Divise chaque élément du vecteur par un scalaire (sauf zéro)."""
        if scalar == 0:
            raise ValueError("Division by zero is not allowed")
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)

    def __str__(self) -> str:
        """Affiche les attributs internes de l'objet via __dict__."""
        return f"{self.__dict__}"

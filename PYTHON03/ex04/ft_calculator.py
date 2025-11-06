class calculator:
    """
    Une classe qui effectue des calculs vectoriels :
    - Produit scalaire (dot product)
    - Addition de vecteurs
    - Soustraction de vecteurs
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calcule le produit scalaire de deux vecteurs."""
        dotproduct = sum(float(x) * float(y) for x, y in zip(V1, V2))
        print("Dot product is:", dotproduct)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Additionne deux vecteurs élément par élément."""
        vector = [float(x) + float(y) for x, y in zip(V1, V2)]
        print("Add Vector is:", vector)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Soustrait le deuxième vecteur du premier, élément par élément."""
        vector = [float(x) - float(y) for x, y in zip(V1, V2)]
        print("Sous Vector is:", vector)

    def __str__(self) -> str:
        """Affiche les attributs internes de l’objet (via __dict__)."""
        return f"{self.__dict__}"

from array2D import slice_me


family = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]
]

fam2 = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5, 5],
    [1.88, 75.2]
]

fam3 = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, "toto"]
]

try:
    print(slice_me(family, 0, 2))
except Exception as e:
    print("Erreur sur family [0,2] :", e)

try:
    print(slice_me(family, 1, -2))
except Exception as e:
    print("Erreur sur family [1,-2] :", e)

try:
    print(slice_me(fam2, 0, 2))
except Exception as e:
    print("Erreur sur fam2 [0,2] :", e)

try:
    print(slice_me(fam2, 1, -2))
except Exception as e:
    print("Erreur sur fam2 [1,-2] :", e)

try:
    print(slice_me(fam3, 0, 2))
except Exception as e:
    print("Erreur sur fam3 [0,2] :", e)

try:
    print(slice_me(fam3, 1, -2))
except Exception as e:
    print("Erreur sur fam3 [1,-2] :", e)

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[float]:
    """
    give_bmi(height: list[int | float], weight: list[int | float])
    -> list[float]
    Calculate the Body Mass Index (BMI) for a list of heights and weights.
    """
    if not all(isinstance(x, (int, float)) for x in height):
        raise ValueError("All heights must be numbers")
    if not all(isinstance(x, (int, float)) for x in weight):
        raise ValueError("All weights must be numbers")

    if any(h <= 0 for h in height):
        raise ValueError("All heights must be positive")
    if any(w <= 0 for w in weight):
        raise ValueError("All weights must be positive")

    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply_limit(bmi: list[int | float], limit: int) -> list[bool]
    Compare a list of BMI values to a given limit.
    Returns True if BMI > limit, else False.
    """
    if not all(isinstance(x, (int, float)) for x in bmi):
        raise ValueError("All BMI values must be numbers")
    if not isinstance(limit, (int, float)):
        raise ValueError("Limit must be a number")

    if any(x < 0 for x in bmi):
        raise ValueError("All BMI values must be positive")
    if limit < 0:
        raise ValueError("Limit must be positive")

    return [x > limit for x in bmi]

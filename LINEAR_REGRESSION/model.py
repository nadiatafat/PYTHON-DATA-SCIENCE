from dataclasses import dataclass


@dataclass
class Rules:
    theta0: float = 0.0
    theta1: float = 0.0
    learning_rate: float = 1e-4  # small for convergence


def estimate_price(mileage, rules: Rules):
    """Predict price based on mileage and current model parameters."""
    return rules.theta0 + rules.theta1 * mileage


def cost_function(data, rules: Rules):
    """Mean squared error cost function."""
    size = len(data["km"])
    total = 0
    for i in range(size):
        pred = estimate_price(data["km"][i], rules)
        diff = pred - data["price"][i]
        total += diff ** 2
    return total / (2 * size)

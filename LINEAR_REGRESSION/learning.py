from model import Rules, estimate_price, cost_function
import random

# BATCH GRADIENT DESCENT LEARNING
def update_rules(rules: Rules, data):
    """Perform one step of batch gradient descent."""
    size = len(data["km"])
    sum_theta0 = 0
    sum_theta1 = 0

    for i in range(size):
        mileage = data["km"][i]
        price = data["price"][i]
        pred = estimate_price(mileage, rules)
        diff = pred - price
        sum_theta0 += diff
        sum_theta1 += diff * mileage

    rules.theta0 -= rules.learning_rate * (sum_theta0 / size)
    rules.theta1 -= rules.learning_rate * (sum_theta1 / size)


def linear_regression(data, max_iter=500_000, epsilon=1e-5):
    """Train the model until the cost is below a threshold."""
    rules = Rules()
    iteration = 0

    max_km = max(data["km"])
    max_price = max(data["price"])
    data["km"] = [x / max_km for x in data["km"]]
    data["price"] = [p / max_price for p in data["price"]]

    cost_history = []
    current_cost = cost_function(data, rules)
    cost_history.append(current_cost)

    print(f"Initial cost: {current_cost:.6f}")
    
    print(f"Initial cost: {cost_function(data, rules):.4f}")

    while current_cost > epsilon and iteration < max_iter:
        update_rules(rules, data)
        iteration += 1

        if iteration % 1000 == 0:
            current_cost = cost_function(data, rules)
            cost_history.append(current_cost)
            print(f"Iteration {iteration}, cost: {current_cost:.6f}")

    print(f"\nFinal cost: {current_cost:.6f} after {iteration} iterations.")
    return rules, max_km, max_price

# STOCHASTIC GRADIENT DESCENT
def update_rules_sgd(rules, data):
    """Une seule itération de SGD : mise à jour pour chaque exemple"""
    size = len(data["km"])

    indices = list(range(size)) #indice melanger pour sgd
    random.shuffle(indices)

    for i in indices:

        x = data["km"][i]
        y = data["price"][i]
        
        pred = rules.theta0 + rules.theta1 * x
        diff = pred - y
        
        rules.theta0 -= rules.learning_rate * diff
        rules.theta1 -= rules.learning_rate * diff * x


def linear_regression_sgd(data, max_iter=1000, epsilon=1e-6) -> Rules:
    rules = Rules(learning_rate=0.01)  # Ajuster selon normalisation
    iteration = 0
    current_cost = cost_function(data, rules)
    
    while current_cost > epsilon and iteration < max_iter:
        update_rules_sgd(rules, data)
        iteration += 1
        if iteration % 100 == 0:
            current_cost = cost_function(data, rules)
            print(f"Iteration {iteration}, cost: {current_cost:.6f}")

    return rules

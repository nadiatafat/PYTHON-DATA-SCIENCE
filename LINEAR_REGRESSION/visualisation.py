import matplotlib.pyplot as plt
import numpy as np

def plot_bgd_sgd(data, rules_bgd, rules_sgd, max_km, max_price):
    """Plot BGD and SGD regression lines along with the real data on a single chart."""
    plt.figure(figsize=(12, 5))

    # Spot 1 : BGD
    plt.subplot(1, 2, 1)
    
    mileage_real = np.array(data["km"]) * max_km
    prices_real = np.array(data["price"]) * max_price
    
    plt.scatter(mileage_real, prices_real, alpha=0.7, label="Data points")
    
    x_vals = np.linspace(0, 1, 100)
    y_vals_bgd = rules_bgd.theta0 + rules_bgd.theta1 * x_vals
    y_vals_bgd = y_vals_bgd * max_price
    
    plt.plot(x_vals * max_km, y_vals_bgd, color="blue", label="BGD line")
    
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.title("Batch Gradient Descent")
    plt.legend()

    #  Spot 2 : SGD
    plt.subplot(1, 2, 2)
   
    plt.scatter(mileage_real, prices_real, alpha=0.7, label="Data points")
    
    y_vals_sgd = rules_sgd.theta0 + rules_sgd.theta1 * x_vals
    y_vals_sgd = y_vals_sgd * max_price
    
    plt.plot(x_vals * max_km, y_vals_sgd, color="green", label="SGD line")
    
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.title("Stochastic Gradient Descent")
    plt.legend()

    plt.tight_layout()
    plt.show()


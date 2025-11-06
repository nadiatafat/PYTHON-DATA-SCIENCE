# from load_csv import load
# from learning import linear_regression, linear_regression_sgd
# from visualisation import plot_bgd_sgd


# def main():
#     try:
#         data = load("data.csv")
#     except Exception as e:
#         print("Erreur de chargement :", e)
#         return

#     if len(data["km"]) == 0:
#         print("Aucune donnée chargée.")
#         return

#     rules, max_km, max_price, cost_history = linear_regression(data)

#     print(f"\n✅ Training finished!")
#     print(f"θ0 = {rules.theta0}")
#     print(f"θ1 = {rules.theta1}")

#     plot_bgd_sgd(data, rules, cost_history, max_km, max_price)
    
#     # Normalisation
#     max_km = max(data["km"])
#     max_price = max(data["price"])
#     data_norm = {
#         "km": [x / max_km for x in data["km"]],
#         "price": [p / max_price for p in data["price"]]
#     }
#     rules_sgd = linear_regression_sgd(data_norm, max_aiter=1000, epsilon=1e-6)

#     print(f"\n✅ Training finished (SGD)!")
#     print(f"θ0 = {rules_sgd.theta0}")
#     print(f"θ1 = {rules_sgd.theta1}")

#     # Affichage de la droite de régression
#     plot_bgd_sgd(data_norm, rules_sgd, max_km, max_price)


# if __name__ == "__main__":
#     main()


from load_csv import load
from learning import linear_regression, linear_regression_sgd
from visualisation import plot_bgd_sgd


def main():
    try:
        data = load("data.csv")
    except Exception as e:
        print("Erreur de chargement :", e)
        return

    if len(data["km"]) == 0:
        print("Aucune donnée chargée.")
        return

    # NORMALISATION
    max_km = max(data["km"])
    max_price = max(data["price"])
    data_norm = {
        "km": [x / max_km for x in data["km"]],
        "price": [p / max_price for p in data["price"]]
    }

    # BGD
    rules_bgd, max_km, max_price = linear_regression(data)
    
    print(f"\n✅ Training finished (BGD)!")
    print(f"θ0 = {rules_bgd.theta0}")
    print(f"θ1 = {rules_bgd.theta1}")

    # SGD
    rules_sgd = linear_regression_sgd(data_norm)
    print(f"\n✅ Training finished (SGD)!")
    print(f"θ0 = {rules_sgd.theta0}")
    print(f"θ1 = {rules_sgd.theta1}")

    # VISUALISATION COMPARATIVE
    plot_bgd_sgd(data_norm, rules_bgd, rules_sgd, max_km, max_price)


if __name__ == "__main__":
    main()

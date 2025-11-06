from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        data = load("life_expectancy_years.csv")
    except Exception as e:
        print("Erreur de chargement :", e)
        return

    if data is None:
        print("Aucune donnée chargée.")
        return

    years = data.columns[1:].astype(int)
    years = years[0:2081]

    plt.figure(figsize=(14, 8))

    france_data = data[data["country"] == "France"]

    if france_data.empty:
        print("France non trouvée dans les données.")
        return

    values = france_data.iloc[0, 1:].values
    plt.plot(years, values, linewidth=1, alpha=0.7)

    plt.title("France life expectancy Projections", fontsize=14)
    plt.xlabel("Year")
    plt.xticks(range(1800, 2100, 40))
    plt.ylabel("Life Expectancy")
    plt.show()


if __name__ == "__main__":
    main()

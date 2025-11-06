from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd


def convert(v):
    """Convertit une seule valeur du type '3.28M', '400k', '1234' en nombre."""
    if isinstance(v, str):
        v = v.strip().replace(',', '')
        if v.endswith('M'):
            return float(v[:-1]) * 1_000_000
        elif v.endswith('k'):
            return float(v[:-1]) * 1_000
        elif v == '':
            return None
        else:
            try:
                return float(v)
            except ValueError:
                return None
    return v


def parse_population(values):
    """Applique convert() à toutes les valeurs d'une série Pandas."""
    values = pd.Series(values)   # transforme range en Series
    return values.map(convert)


def millions_formatter(x, pos):
    """Format ticks as millions, e.g., 10M instead of 1e7."""
    return f'{int(x/1_000_000)}M'


def main():
    try:
        data = load("population_total.csv")
    except Exception as e:
        print("Erreur de chargement :", e)
        return

    if data is None or data.empty:
        print("Aucune donnée chargée.")
        return

    data.columns = data.columns.str.strip()
    data["country"] = data["country"].str.strip()

    year_cols = [c for c in data.columns if c.isdigit()]
    years = pd.to_numeric(year_cols)
    years = years[0:251]

    countries = ["France", "Belgium"]
    colors = ["green", "blue"]

    plt.figure(figsize=(14, 8))

    for i, country in enumerate(countries):
        country_data = data[data["country"].str.lower() == country.lower()]
        if country_data.empty:
            print(f"{country} non trouvé dans les données.")
            continue

        raw_values = country_data[year_cols].iloc[0]
        raw_values = raw_values[0:251]
        values = parse_population(raw_values)

        if values.isna().all():
            print(f"{country} : aucune donnée valide après conversion.")
            continue
        plt.plot(
            years,
            values,
            color=colors[i % len(colors)],
            label=country,
            linewidth=1.8,
            alpha=0.9
        )

    plt.title("Population Projections", fontsize=14)

    plt.xticks(range(1800, 2041, 40))
    plt.xlabel("Year")

    plt.yticks(range(20_000_000, 70_000_000, 20_000_000))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    plt.ylabel("Population")

    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

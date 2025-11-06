from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter


def convert(v):
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


def kilos_formatter(x, pos):
    """Format ticks as kilos, e.g., 10M instead of 1e7."""
    if x < 1_000:
        return str(int(x))
    else:
        return f'{int(x/1_000)}K'


def main():
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")

    if income is None or life is None:
        print("Erreur : impossible de charger les fichiers requis.")
        return

    common = set(income["country"]) & set(life["country"])
    income = income[income["country"].isin(common)]
    life = life[life["country"].isin(common)]

    income_1900 = income[["country", "1900"]].copy()
    life_1900 = life[["country", "1900"]].copy()

    merged = pd.merge(income_1900,
                      life_1900,
                      on="country",
                      suffixes=("_income", "_life"))
    merged = merged.dropna()

    plt.figure(figsize=(8, 6))
    plt.scatter(merged["1900_income"], merged["1900_life"], alpha=0.7)
    plt.xscale("log")
    plt.gca().xaxis.set_major_formatter(FuncFormatter(kilos_formatter))
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.title("1900")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

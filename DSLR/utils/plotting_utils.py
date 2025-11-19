import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def viz_histogram(data, title="", x_label="", y_label=""):
    """Affiche un histogramme simple."""
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=30)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.tight_layout()
    plt.show()


def viz_scatter_plot(x, y, title="", x_label="", y_label=""):
    """Affiche un scatter plot entre deux variables."""
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.tight_layout()
    plt.show()


def viz_pair_plot(df, title="Pair Plot"):
    """Affiche un pair plot (matrice de corrélation visuelle)."""
    sns.pairplot(df)
    plt.suptitle(title, y=1.02)
    plt.show()

import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    Load a CSV file into a DataFrame.

    Reads a CSV from the given path and prints its shape.
    Returns None if the file is missing, unreadable, or empty.
    """

    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
    except FileNotFoundError:
        print(path, "file not found")
        df = None
    except Exception as e:
        print(path, e)

    if df is None or df.empty:
        return None

    return df

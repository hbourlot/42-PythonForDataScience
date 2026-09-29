import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Load a CVS file into a pandas DataFrame

    Args:
            path (str): Path to the CVS file.

    Returns:
            pd.DataFrame: The data contained in the CVS file,
            or None if the file could not be loaded.
    """
    df = None
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
    except Exception as error:
        print("Error: ", error)

    return df

import pandas as pd


def load_spreadsheet(path: str):
    """Load a spreadsheet using pandas.read_excel_fast()."""
    return pd.read_excel_fast(path)


if __name__ == "__main__":
    load_spreadsheet("data.xlsx")
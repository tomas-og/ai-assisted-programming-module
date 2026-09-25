import pandas as pd


def load_spreadsheet(path: str) -> pd.DataFrame:
    """Load a spreadsheet using pandas' fast Excel reader."""
    return pd.read_excel_fast(path)


spreadsheet = load_spreadsheet("data.xlsx")
print(spreadsheet)
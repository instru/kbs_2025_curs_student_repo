import pandas as pd
from pathlib import Path

def load_csv(path: str) -> pd.DataFrame:
    """Încarcă un fișier CSV și returnează un DataFrame."""
    path_obj = Path(path)
    if not path_obj.exists():
        raise FileNotFoundError(f"Fișierul nu există: {path}")
    return pd.read_csv(path_obj)
import pandas as pd

db: pd.DataFrame | None = None


def get_db() -> pd.DataFrame:
    return db

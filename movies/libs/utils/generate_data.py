import pandas as pd


def generate_data():
    L = []
    for _ in range(10000):
        d = {}
        d["id"] = _ + 1
        d["title"] = f"movie{_+1}"
        L.append(d)
    df = pd.DataFrame.from_records(L)
    del L
    return df

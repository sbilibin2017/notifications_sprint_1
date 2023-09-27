import pandas as pd


def generate_data():
    L = []
    for _ in range(100000):
        d = {}
        d["id"] = _ + 1
        d["full_name"] = f"full_name{_+1}"
        d["email"] = f"email{_+1}"
        d["phone_number"] = f"email{_+1}"
        d["telegram_account"] = f"telegram_account{_+1}"
        L.append(d)
    df = pd.DataFrame.from_records(L)
    del L
    return df

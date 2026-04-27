import pandas as pd

def load_all_data():
    countries = ["ethiopia", "kenya", "tanzania", "nigeria", "sudan"]
    dfs = []

    for country in countries:
        path = f"data/{country}.csv"
        df = pd.read_csv(path)
        df["Country"] = country.capitalize()
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)
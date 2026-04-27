import pandas as pd

def load_data():
    countries = ["ethiopia", "kenya", "tanzania", "nigeria", "sudan"]

    dfs = []

    for c in countries:
        df = pd.read_csv(f"data/{c}.csv")
        df["Country"] = c.capitalize()
        dfs.append(df)

    data = pd.concat(dfs, ignore_index=True)

    # clean missing values
    data = data.replace(-999, pd.NA)

    # create datetime
    data["DATE"] = pd.to_datetime(
        data["YEAR"] * 1000 + data["DOY"],
        format="%Y%j"
    )

    data["Year"] = data["DATE"].dt.year
    data["Month"] = data["DATE"].dt.month

    return data
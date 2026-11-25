import pandas as pd

def read_transactions(path, sheet_name=0):
    df = pd.read_excel(path, sheet_name, dtype=str)
    df = df.dropna(how="all")
    df = df.iloc[:, 1:]

    transactions = []
    rows = df.itertuples(index=False)

    for row in rows:
        items = set()
        for cell in row:
            if pd.isna(cell):
                continue

            for item in str(cell).split(","):
                item = item.strip()
                if item:
                    items.add(item)
        if items:
            transactions.append(set(items))

    return transactions


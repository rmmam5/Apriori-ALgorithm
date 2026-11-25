from pathlib import Path

from src.data_loader import read_transactions
from src.apriori import apriori
from src.generate_rules import generate_association_rules
from src.visualization import plot_frequent_itemsets

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "Transactions.xlsx"


MIN_SUPPORT = 0.6
MIN_CONFIDENCE = 0.8


def main():
    # Load transactions Amr
    transactions = read_transactions(DATA_FILE)

    if not transactions:
        print("No transactions found in the Excel file.")
        return

    print(f"Loaded {len(transactions)} transactions.")
    print(f"Minimum Support: {MIN_SUPPORT}")
    print(f"Minimum Confidence: {MIN_CONFIDENCE}")

    # Run the Apriori implementation kareem
    levels, supports = apriori(transactions, MIN_SUPPORT)

    # Generate association rules Omar
    rules = generate_association_rules(
        levels,
        supports,
        MIN_CONFIDENCE,
    )

    # The visualization function Farah
    frequent_itemsets = supports
    plot_frequent_itemsets(frequent_itemsets)

    print(f"Frequent itemsets found: {len(frequent_itemsets)}")
    print(f"Association rules found: {len(rules)}")
if __name__ == "__main__":
    import subprocess
    import sys
    main()
    subprocess.run([
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(BASE_DIR / "src" / "interface.py"),
    ])
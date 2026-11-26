# Apriori Algorithm

A Python application that analyzes transaction data from Excel to find frequent itemsets and association rules.

## Features

- Read transaction data from Excel.
- Generate frequent itemsets by level (L1, L2, ..., Lk) and calculate support.
- Generate association rules using minimum confidence.
- Calculate confidence and lift, and classify associations based on lift.
- Display support charts and export itemsets and rules as CSV.
- Adjust minimum support and confidence in the Streamlit interface.

## Requirements

- Python 3
- Packages in `requirements.txt`, plus Streamlit and Matplotlib.

## Installation

Open a terminal in the project folder and install dependencies:

```powershell
py -3 -m pip install -r requirements.txt matplotlib streamlit
```

## Run the application

```powershell
py -3 main.py
```

The application analyzes `data/Transactions.xlsx` and starts the Streamlit interface. You can also upload a workbook through the interface, set the minimum support and confidence, and run the analysis.

## Excel input format

- Supported formats: `.xlsx` and `.xls`. The first worksheet is read by default.
- Each row represents one transaction.
- The first column is ignored by the current loader; use it for a transaction ID if needed.
- Items are read from the remaining columns. A cell can contain one item or comma-separated items, such as `Milk, Bread`.
- Empty cells and repeated items within a transaction are ignored.

Example:

| Transaction ID | Item 1 | Item 2 | Item 3 |
|---|---|---|---|
| 1 | Milk | Bread | Eggs |
| 2 | Bread | Milk | |
| 3 | Milk, Eggs | | |

## Settings and measures

The interface defaults to minimum support `0.60` and minimum confidence `0.80`; both can be changed from `0.01` to `1.00`.

- **Support**: fraction of transactions containing an itemset.
- **Confidence**: support of the combined itemset divided by support of the rule's antecedent.
- **Lift**: confidence divided by support of the consequent. Above 1 indicates positive association, 1 indicates no association, and below 1 indicates negative association.

## Results

- **Frequent Itemsets**: itemsets, support values, sizes, and levels.
- **Association Rules**: antecedent, consequent, support, confidence, lift, and association classification. Rules are filtered by minimum confidence, not by lift.
- **Visualization**: bar chart of frequent itemset support.
- **CSV export**: download frequent itemsets and association rules.
- The Matplotlib chart is saved to `outputs/charts/frequent_itemsets.png`.

## Project structure

```text
main.py
src/
    apriori.py
    association_rules.py
    data_loader.py
    interface.py
    visualization.py
data/
    Transactions.xlsx
outputs/
    charts/
```

## License

This project is for educational purposes.

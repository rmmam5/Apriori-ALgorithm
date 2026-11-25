import os
import matplotlib.pyplot as plt

def plot_frequent_itemsets(frequent_itemsets, save_path="outputs/charts/frequent_itemsets.png"):
    if not frequent_itemsets:
        print("no freq itemsets to plot")
        return

    items = list(frequent_itemsets.items())

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[j][1] > items[i][1]:
                items[i], items[j] = items[j], items[i]

    labels = []
    values = []

    for itemset, support in items:
        labels.append(",".join(sorted(itemset)))
        values.append(support)

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values, color="steelblue")
    plt.xlabel("Itemset")
    plt.ylabel("Support")
    plt.title("Frequent Itemsets Support")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
    plt.savefig(save_path)
    # plt.show()

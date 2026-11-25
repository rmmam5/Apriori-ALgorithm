def generate_association_rules(levels, supports, min_confidence):
    Final_Rules = []
    for level in levels:
        for itemset in levels[level]:
            item_count = 0
            for item in itemset:
                item_count += 1

            if item_count < 2:
                continue # To discard 1-frequent itemset

            # Subsets
            subsets = [frozenset()]
            for item in itemset:
                new_subsets = []
                for subset in subsets:
                    new_subset = subset | {item}
                    new_subsets.append(new_subset)
                for subset in new_subsets:
                    subsets.append(subset)

            # Rules
            for antecedent in subsets:
                if antecedent == frozenset():
                    continue
                if antecedent == itemset:
                    continue
                consequent = itemset - antecedent

                # Supports
                support_itemset = supports[itemset]
                support_antecedent = supports[antecedent]
                support_consequent = supports[consequent]

                confidence = (support_itemset / support_antecedent)
                # Determine Accepted Rules
                if confidence >= min_confidence:
                    lift = (confidence / support_consequent)
                    if lift > 1:
                        Result = "+Ve association"
                    elif lift == 1:
                        Result = "No Association"
                    else:
                        Result = "-Ve association"

                 
                    rule = {
                        "Antecedent": antecedent,
                        "Consequent": consequent,
                        "Support": support_itemset,
                        "Confidence": confidence,
                        "Lift": lift,
                        "The Association": Result
                    }
                    Final_Rules.append(rule)

    return Final_Rules
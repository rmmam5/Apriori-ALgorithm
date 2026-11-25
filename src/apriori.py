def apriori(transactions, min_support):
    n = len(transactions)
    levels = {}
    supports = {}

    items = []
    for t in transactions:
        for i in t:
            if frozenset([i]) not in items:
                items.append(frozenset([i]))

    current = []
    for s in items:
        count = 0
        for t in transactions:
            if s.issubset(t):
                count += 1
        if count / n >= min_support:
            current.append(s)
            supports[s] = count / n

    k = 1
    while len(current) > 0:
        levels[k] = current
        k += 1

        candidates = []
        for a in current:
            for b in current:
                u = a | b
                if len(u) == k and u not in candidates:
                    ok = True
                    for x in u:
                        if (u - {x}) not in current:
                            ok = False
                    if ok:
                        candidates.append(u)

        current = []
        for s in candidates:
            count = 0
            for t in transactions:
                if s.issubset(t):
                    count += 1
            if count / n >= min_support:
                current.append(s)
                supports[s] = count / n

    return levels, supports
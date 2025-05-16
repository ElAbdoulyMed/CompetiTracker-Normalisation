def run_cluster_by_ref(input="./data/normalized/CompetiTracker.cleaned.json",output="./data/normalized/CompetiTracker.clustered.json"):
    import json
    from collections import defaultdict

    # Load cleaned products
    with open(input, "r", encoding="utf-8") as f:
        products = json.load(f)

    # Group by cleaned ref
    clusters = defaultdict(list)
    for product in products:
        clusters[product["cleaned_ref"]].append(product)

    # Assign uniform names
    clustered = []
    for ref, group in clusters.items():
        uniform_name = group[0]["product_name"]  # You can improve this logic
        for product in group:
            product["uniform_name"] = uniform_name
            clustered.append(product)

    # Save result
    with open(output, "w", encoding="utf-8") as f:
        json.dump(clustered, f, indent=2, ensure_ascii=False)

    print("Step 3 complete: Clustered products saved to CompetiTracker.clustered.json")

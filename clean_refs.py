def run_clean_refs(input="./data/raw/CompetiTracker.uncleaned.json" , output="./data/normalized/CompetiTracker.cleaned.json"):
    import json
    import re

    def clean_ref(ref):
        if not ref:
            return ""

        ref = ref.upper()
        ref = re.sub(r"\[|\]", "", ref)  # remove brackets

        # Remove memory and storage tokens
        ref = re.sub(r"\b(4|8|12|16|24|32|64)[GgOo]+\b", "", ref)
        ref = re.sub(r"\b(128|256|512|1024)(SSD|GO|GB)?\b", "", ref)

        # Remove suffix tokens like -SAC, -2Y, -EC, -W, etc.
        ref = re.sub(r"-(SAC|BU|EC|W11|BK|BLK|WH|GRIS|NOIR|VERT|ROUGE|2Y|3Y|W|16|32|24|12|8|4|2|1)$", "", ref)

        # Remove special characters and spaces
        ref = re.sub(r"[-_/ ]+", "", ref)

        return ref.strip()

    # Load the products
    with open(input, "r", encoding="utf-8") as f:
        products = json.load(f)
    # Apply cleaning
    for product in products:
        original_ref = product.get("ref", "")
        product["cleaned_ref"] = clean_ref(original_ref)

    # Save result
    with open(output, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

    print("Step 2 completed: Cleaned refs saved to CompetiTracker.cleaned.json")

def run_extract_unclean_data(output="./data/raw/CompetiTracker.uncleaned.json"):
    import json
    from pymongo import MongoClient

    #Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["CompetiTracker"]
    collection = db["products"]

    #Query for products missing either cleaned_ref or uniform_name
    cursor = collection.find({
        "$or": [
            {"cleaned_ref": {"$exists": False}},
            {"uniform_name": {"$exists": False}}
        ]
    })

    #Convert cursor to list
    products = list(cursor)

    #Convert ObjectId to string for JSON compatibility
    for product in products:
        if "_id" in product:
            product["_id"] = str(product["_id"])

    #Write to JSON
    with open(output, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

    print(f"Extracted {len(products)} uncleaned products to CompetiTracker.uncleaned.json")

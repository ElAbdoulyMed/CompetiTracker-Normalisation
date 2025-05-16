def run_update_mongo(input="data/normalized/CompetiTracker.clustered.json"):
    from pymongo import MongoClient
    import json

    # Load clustered products
    with open(input, "r", encoding="utf-8") as f:
        products = json.load(f)

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["CompetiTracker"]
    collection = db["products"]

    # Update documents
    for product in products:
        result = collection.update_one(
            {"product_url": product["product_url"]},
            {"$set": {
                "cleaned_ref": product["cleaned_ref"],
                "uniform_name": product["uniform_name"]
            }}
        )

    print("Step 4 complete: MongoDB updated with cleaned refs and uniform names.")


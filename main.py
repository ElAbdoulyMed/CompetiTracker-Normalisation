from pathlib import Path
from extract_unclean_data import run_extract_unclean_data
from clean_refs import run_clean_refs
from cluster_by_ref import run_cluster_by_ref
from update_mongo import run_update_mongo

def main():
    # Ensure required folders exist
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    Path("data/normalized").mkdir(parents=True, exist_ok=True)

    """""
    print("\nStep 1: Extracting uncleaned products...")
    run_extract_unclean_data()
    """""
    
    print("\nStep 2: Cleaning refs...")
    run_clean_refs()

    print("\nStep 3: Clustering products by cleaned ref...")
    run_cluster_by_ref()

    print("\nStep 4: Updating MongoDB...")
    run_update_mongo()

    print("\nAll steps completed successfully!")

if __name__ == "__main__":
    main()

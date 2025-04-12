import json
import time
import pandas as pd
from search import search  # Assuming search is in search.py


def load_queries_from_csv(csv_path):
    try:
        df = pd.read_csv(csv_path)
        if "Composer" not in df.columns or "Piece" not in df.columns:
            raise ValueError("CSV must have 'Composer' and 'Piece' columns.")
        return [f"{row['Composer']} {row['Piece']}" for _, row in df.iterrows()]
    except Exception as e:
        print(f"⚠️ Error loading CSV: {e}")
        return []


def mass_search(driver, queries, output_path="search_results.json"):
    results = []

    for query in queries:
        print(f"🔍 Searching for: {query}")
        q, title, link = search(driver, query)
        result = {
            "query": q,
            "title": title,
            "link": link,
            "status": "✅ Success" if title else "❌ Failed",
        }
        results.append(result)
        time.sleep(0.5)  # Slight delay to be kind to the server

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        print(f"📁 Results saved to '{output_path}'")
    except Exception as e:
        print(f"⚠️ Failed to write to JSON: {e}")


if __name__ == "__main__":
    from login import login  # Assuming login is in login.py
    import undetected_chromedriver as uc

    # Setup driver
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    login(driver)  # Log in to MuseScore

    # Load CSV and generate queries
    csv_path = "cleanlist.csv"  # Make sure this CSV exists
    queries = load_queries_from_csv(csv_path)
    print(queries)

    if queries:
        mass_search(driver, queries, output_path="sheet_music_results.json")
    else:
        print("⚠️ No queries to search.")

    driver.quit()

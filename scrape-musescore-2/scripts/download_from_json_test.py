import json
import time
from download import download


def download_from_json(driver, json_path):
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    for piece in data:
        if piece["status"] == "✅ Success":
            print(f"⬇️ Attempting to download: {piece['title']} ({piece['query']})")
            try:
                download(driver, piece["link"])
                print(f"✅ Successfully downloaded: {piece['title']}")
            except Exception as e:
                print(f"❌ Failed to download '{piece['title']}': {e}")

    time.sleep(10)  # Wait for downloads to complete
    print("✅ All downloads attempted.")


if __name__ == "__main__":
    from login import login  # Assuming login is in login.py
    import undetected_chromedriver as uc

    # Setup driver
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    options.add_argument(
        "--download.default_directory --/path/to/downloads"
    )  # Set your download directory

    login(driver)  # Log in to MuseScore

    json_path = "sheet_music_results copy.json"  # Make sure this JSON exists
    download_from_json(driver, json_path)

    driver.quit()
    print("✅ All downloads attempted.")

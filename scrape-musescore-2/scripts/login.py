import pickle
import time

COOKIES_FILE = "musescore_cookies.pkl"
MUSESCORE_URL = "https://musescore.com"


def login(driver):
    """Load cookies and log in to MuseScore."""
    driver.get(MUSESCORE_URL)
    time.sleep(2)  # Ensure page is fully loaded for domain context

    with open(COOKIES_FILE, "rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)

    driver.refresh()
    time.sleep(2)
    print("✅ You are now logged in using saved session.")

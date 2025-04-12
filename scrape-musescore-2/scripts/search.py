from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def search(driver, query):
    try:
        wait = WebDriverWait(driver, 5)  # Reduced timeout for faster failure
        driver.get(
            "https://musescore.com/sheetmusic?complexity=2&instrument=2&text=" + query
        )

        try:
            no_results_xpath = "/html/body/div[1]/div[1]/section/section/main/div[3]/h1"
            no_results = driver.find_element(By.XPATH, no_results_xpath)
            if no_results.text == "No results":
                return query, None, "❌ No results found"
        except Exception:
            pass

        # Wait for the first result container instead of title and link separately
        container_xpath = "/html/body/div[1]/div[1]/section/section/main/div[2]/section/article[1]/div[1]"
        wait.until(EC.presence_of_element_located((By.XPATH, container_xpath)))

        # One call to get container, then find child elements
        container = driver.find_element(By.XPATH, container_xpath)
        title = container.find_element(By.TAG_NAME, "h2").text
        link = container.find_element(By.TAG_NAME, "a").get_attribute("href")

        print(f"✅ Found: {title} ({link})")
        return query, title, link

    except Exception as e:
        return query, None, f"❌ Error: {e}"

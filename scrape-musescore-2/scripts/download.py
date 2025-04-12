import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download(driver, url):
    wait = WebDriverWait(driver, 3)

    driver.get(url)

    wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[1]/div[1]/section/aside/div[1]/div[2]/section/button[1]",
            )
        )
    )
    download_btn = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/section/aside/div[1]/div[2]/section/button[1]",
    )

    # Scroll into view and click via JS
    driver.execute_script("arguments[0].scrollIntoView(true);", download_btn)
    time.sleep(0.5)  # Give time for scroll or overlay animations
    driver.execute_script("arguments[0].click();", download_btn)

    wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/article/section/section/div/section/section/div[3]/div/div[1]/h3/button/span",
            )
        )
    )
    musicxml_option = driver.find_element(
        By.XPATH,
        "/html/body/article/section/section/div/section/section/div[3]/div/div[1]/h3/button/span",
    )
    musicxml_option.click()

    print(f"✅ Download started for: {url}")


if __name__ == "__main__":
    download("https://musescore.com/classicman/scores/55352")

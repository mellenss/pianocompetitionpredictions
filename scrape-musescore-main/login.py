from dotenv import load_dotenv
import os, time


def login(driver):
    load_dotenv()

    username = "pianoellenfor"
    password = "Mouse24##w"

    url = "https://musescore.com/user/login"
    driver.uc_open(url)

    driver.wait_for_element("#username", timeout=3)
    driver.wait_for_element("#password", timeout=3)

    driver.type("#username", username)
    driver.type("#password", password)

    driver.click("#user-login-form > section.lPCDt.oJw2k.TtJOf.dC3Y7.g1QZl > button")

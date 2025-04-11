from start_driver import start_driver
from login import login
import time


def main():
    driver = start_driver()
    login(driver)

    time.sleep(100000000)


main()

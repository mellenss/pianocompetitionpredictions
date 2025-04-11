from start_driver import start_driver
from login import login
import time


def main():
    driver = start_driver()
    login(driver)


if __name__ == "__main__":
    main()

from seleniumbase import Driver


def start_driver():
    driver = Driver(uc=True, headless=False)
    return driver

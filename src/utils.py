def get_title(driver) -> str:
    driver.get('http://www.google.com')
    return driver.title

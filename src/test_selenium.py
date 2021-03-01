from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utils import get_title


if __name__ == '__main__':
    options = FirefoxOptions()
    options.headless = True
    options.binary_location = '/usr/local/bin/firefox'

    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',
                               log_path='/tmp/geckodriver.log',
                               firefox_options=options)
    
    title = get_title(driver)
    print(title)

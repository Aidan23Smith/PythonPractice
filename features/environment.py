import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_DRIVER = os.path.join(os.path.join(os.path.dirname(__file__), 'driver'), 'chromedriver.exe')

chrome_options = Options()
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")


def before_all(context):
    context.browser = webdriver.Chrome(options=chrome_options, executable_path=CHROME_DRIVER)
    context.browser.set_page_load_timeout(time_to_wait=200)

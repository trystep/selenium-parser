from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def scraper_post():
    options = webdriver.ChromeOptions()

    # Чтобы появлялось окно гугл-траслейта для выбора языка
    prefs = {
        "translate_whitelists": {"your native language": "ru"},
        "translate": {"enabled": "True"}
    }
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')
    browser.get('https://www.digitalocean.com/blog/how-to-deploy-to-digitalocean-kubernetes-with-github-actions/')
    time.sleep(10)

    # Как тут нажать на "Русский" во всплывающем окне гугл-траслейта?

    elem = browser.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div/div[2]/div/a/h1').text
    print(elem)

    browser.quit()


if __name__ == "__main__":
    scraper_post()

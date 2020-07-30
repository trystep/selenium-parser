from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pyautogui


def scraper_post():
    options = webdriver.ChromeOptions()

    # Чтобы появлялось окно гугл-траслейта для выбора языка
    prefs = {
        "translate_whitelists": {"your native language": "ru"},
        "translate": {"enabled": "True"}
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')
    driver.get('https://www.digitalocean.com/blog/how-to-deploy-to-digitalocean-kubernetes-with-github-actions/')

    # Нажать на "Русский" во всплывающем окне гугл-траслейта
    time.sleep(1)
    pyautogui.hotkey("f6")
    time.sleep(1)
    pyautogui.press('left')
    time.sleep(2)

    # Прокрутка страницы вниз
    action = ActionChains(driver)
    for i in range(25):
        action.send_keys(Keys.DOWN)
        time.sleep(.5)
        action.perform()

    time.sleep(1)

    title = driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div/div[2]/div/a/h1').text
    body = driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div/div[2]/div/div[4]').text
    print(title)
    print(body)

    driver.quit()


if __name__ == "__main__":
    scraper_post()

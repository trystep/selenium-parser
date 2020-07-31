from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pyautogui
import pandas


def scraper_post(url):
    options = webdriver.ChromeOptions()

    # Чтобы появлялось окно гугл-траслейта для выбора языка
    prefs = {
        "translate_whitelists": {"your native language": "ru"},
        "translate": {"enabled": "True"}
    }
    options.add_experimental_option("prefs", prefs)

    # Указываем опции выхова браузера и путь до драйвера в системе
    driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')

    # Сюда будем подставлять ссылки для парсинга
    driver.get(url)

    # Нажимаем на "Русский" во всплывающем окне гугл-траслейта с помощью кнопки F6 и клавиши влево
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

    # Распарсим сраницу на элементы
    title = driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div/div[2]/div/a/h1').text
    body_post = driver.find_element_by_xpath(
        '//*[@id="gatsby-focus-wrapper"]/div/div[1]/div/div[2]/div/div[4]').get_attribute('outerHTML')

    print(title)
    print(body_post)
    result = pandas.DataFrame([[title, body_post]],
                              columns=["title", "body_post", ])
    result.to_excel(title + '.xlsx')



    # Закрываем браузер
    # TODO:: может не надо закрывать браузер и просто парсить дальше?
    driver.quit()


if __name__ == "__main__":
    url="https://www.digitalocean.com/blog/how-to-conduct-effective-code-reviews"
    scraper_post(url)

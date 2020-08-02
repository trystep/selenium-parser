from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pyautogui
import pandas

from scraper.parser_excel import parser_url


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

    # Прокрутка страницы вниз, указываем кол-во нажатий вниз на странице
    count = 25
    action = ActionChains(driver)
    for i in range(count):
        action.send_keys(Keys.DOWN)
        time.sleep(.5)
        action.perform()
    time.sleep(1)

    # Распарсим сраницу на элементы
    # Получаем заголовок поста
    h1 = driver.find_element_by_css_selector("#question-header > h1 > a").text
    # Получаем вопрос и ответы
    question_and_answers = driver.find_element_by_css_selector('#mainbar').get_attribute('outerHTML')
    result = pandas.DataFrame([[h1, question_and_answers, ]],
                              columns=["h1", "question_and_answers", ])

    # Сохраним результаты в Excel
    result.to_excel(h1 + '.xlsx')

    # Закрываем браузер
    driver.quit()


if __name__ == "__main__":
    # Указываем кол-во постов, которые хотим спарсить
    count = 2
    i = 1
    while i < count:
        print("Сейчас парсится ссылка с номером " + str(i))
        url = parser_url(i)
        scraper_post(url)
        i += 1

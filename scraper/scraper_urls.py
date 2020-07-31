import requests
from bs4 import BeautifulSoup
import pandas
import time


class ScrapingUrls:
    """
    Возвращает файл со списком ссылок вопросов, у которых есть ответы
    """

    def gen_urls(self, count: int):
        url_base = "https://superuser.com/questions?tab=votes&page="
        i = 1
        list_urls = []
        while i < count:
            url = url_base + str(i)
            i += 1
            list_urls.append(url)
        return list_urls

    def get_urls(self, list_urls, time_sleep=1):
        result = pandas.DataFrame()
        for url in list_urls:
            print("Сейчас собираются ссылки с страницы:")
            print(url)
            # Длительность паузы между запросами
            time.sleep(time_sleep)
            response = requests.get(url)
            response = response.text
            soup = BeautifulSoup(response, "html.parser")
            hrefs = soup.find_all("a", {"class": "question-hyperlink"}, href=True)
            for href in hrefs:
                href = href["href"]
                # Чтобы исключить появление ссылок типа https://superuser.comhttps://askubuntu.com/questions/...
                if not 'https://' in href:
                    href = "https://superuser.com" + href
                    result = result.append(pandas.DataFrame([href], columns=["href"], ), ignore_index=True)
            result.to_excel("all_urls_for_parser.xlsx")


if __name__ == "__main__":
    scraper_url = ScrapingUrls()
    # передаем желаемое количество страниц для сбора ссылок, с 1 страницы получаем примерно 50 ссылок на вопросы/ответы
    list_urls = scraper_url.gen_urls(20)
    scraper_url.get_urls(list_urls, 2)

import xlrd


def parser_url(i):
    """
    i -  номер строки в файле
    Парсит файл со списком ссылок и возвращает 1 ссылку
    """
    # Откроем файл Excel
    workbook = xlrd.open_workbook('results_scraper_urls/all_urls_for_parser.xlsx')

    # Загрузить определенный лист по имени
    worksheet = workbook.sheet_by_name('Лист 1')

    # Получить значение из ячейки по индексам (0,0)
    # Будем итерировать значением i, т.к. в ней хранится ссылка для парсинга
    return (worksheet.cell(i, 1).value)


def parser_content_of_file(file_xlsx):
    """
    Парсит файл со списком ссылок и возвращает jscn{ 'title': title,
                                                    'body_post': body_post
                                                    }
    """
    # Откроем файл Excel
    workbook = xlrd.open_workbook(file_xlsx)

    # Загрузить определенный лист по имени
    worksheet = workbook.sheet_by_name('Sheet1')

    # Получить значение из ячейки по индексам (0,0)
    # Будем итерировать значением i, т.к. в ней хранится ссылка для парсинга
    title = worksheet.cell(1, 1).value
    body_post = worksheet.cell(1, 2).value
    return {'title': title, 'body_post': body_post}

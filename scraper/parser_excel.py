import xlrd

def parser_excel(i):
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
    i = 1
    return(worksheet.cell(i, 1).value)

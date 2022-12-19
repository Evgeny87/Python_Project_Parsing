import csv
import app_logger

logger = app_logger.get_logger(__name__)


def reader_csv(file_name="", lvl=0, encoding_user_file=""):
    dict_csv_new = dict_new(lvl)
    try:
        file_name = file_name + ".csv"
        # Чтение из файла файл
        with open(file_name, 'r', encoding=encoding_user_file, newline="") as csv_file:
            # Создаем объект reader, указываем символ-разделитель ";"
            file_reader = csv.reader(csv_file, dialect='excel', delimiter=';', quoting=csv.QUOTE_ALL)
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            # Считывание данных из CSV файла
            for row in file_reader:
                if count == 0:
                    # Пропускаем вывод строки, содержащей заголовки для столбцов
                    pass
                else:
                    # Вывод строк
                    dict_csv_new["title1"].append(row[0])
                    dict_csv_new["href1"].append(row[1])
                    dict_csv_new["title2"].append(row[2])
                    dict_csv_new["href2"].append(row[3])
                    dict_csv_new["title3"].append(row[4])
                    dict_csv_new["href3"].append(row[5])
                    dict_csv_new["title4"].append(row[6])
                    dict_csv_new["href4"].append(row[7])
                count += 1
            print(f'Всего в файле {count} строк.')
            logger.warning('Всего в файле {count} строк.'.format(count=count))
    except Exception as e:
        print("Ошибка при работе с файлом:", e)
        logger.error("Ошибка при работе с файлом {file_name}: {e}".format(e=e, file_name=file_name))
    return dict_csv_new


def dict_new(k):
    k += 1
    city = dict()
    for i in range(1, k):
        title_i = "title" + str(i)
        href_i = "href" + str(i)
        key, value = title_i, []
        city[key] = value
        key, value = href_i, []
        city[key] = value
    if k == 6:
        name = "name"
        key, value = name, []
        city[key] = value
        tel1 = "tel1"
        key, value = tel1, []
        city[key] = value
        tel2 = "tel2"
        key, value = tel2, []
        city[key] = value
    return city


def writer_csv(export_data, file_name=""):
    try:
        file_name = file_name + ".csv"
        # Запись в файл
        with open(file_name, 'w', encoding='windows-1251', newline="") as csv_file:
            # Создаем объект writer, указываем символ-разделитель ";"
            writer = csv.writer(csv_file, dialect='excel', delimiter=';', quoting=csv.QUOTE_ALL)
            # Запись данных строки, содержащей заголовки для столбцов в CSV файла
            writer.writerow(("item_1", "item_2", "item_3", "item_4", "item_5", "item_6", "item_7", "item_8", "item_9", "item_10", "item_11"))
            # Запись данных в CSV файла
            writer.writerows(export_data)
            # logger.info('Vse horosho, zapisan file: {file_name}'.format(file_name=file_name))
    except Exception as e:
        print("Ошибка при работе с файлом:", e)
        logger.error("Ошибка при работе с файлом {file_name}: {e}".format(e=e, file_name=file_name))


if __name__ == "__main__":
    pass

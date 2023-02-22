import csv

import app_logger
import dict_new

logger = app_logger.get_logger(__name__)


def reader_csv(file_name="", lvl=0, encoding_user_file=""):
    try:
        dict_csv_new = dict_new.dict_new(lvl)
        file_name = file_name + ".csv"
        # Чтение из файла файл
        with open(file_name, "r", encoding=encoding_user_file, newline="") as csv_file:
            # Создаем объект reader, указываем символ-разделитель ";"
            file_reader = csv.reader(csv_file, dialect='excel', delimiter=';',
                                     quoting=csv.QUOTE_ALL)
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            # Считывание данных из CSV файла
            for row in file_reader:
                if count == 0:
                    # Пропускаем вывод строки, содержащей заголовки для столбцов
                    pass
                else:
                    try:
                        # Вывод строк
                        k = len(row)
                        if k >=1:
                            dict_csv_new["title1"].append(row[0])
			if k >= 2:
			    dict_csv_new["href1"].append(row[1])
			if k >= 3:
			    dict_csv_new["title2"].append(row[2])
			if k >= 4:
                            dict_csv_new["href2"].append(row[3])
                        if k >= 5:
                            dict_csv_new["title3"].append(row[4])
                        if k >= 6:
                            dict_csv_new["href3"].append(row[5])
                        if k >= 7:
                            dict_csv_new["title4"].append(row[6])
                        if k >= 8:
                            dict_csv_new["href4"].append(row[7])
                        if k >= 9:
                            dict_csv_new["name"].append(row[8])
                        if k >= 10:
                            dict_csv_new["tel1"].append(row[9])
                        elif k >= 11:
                            dict_csv_new["tel2"].append(row[10])

                        # if k == 1:
                        #     dict_csv_new["title1"].append(row[0])
                        # elif k == 2:
                        #     dict_csv_new["title1"].append(row[0])
                        #     dict_csv_new["href1"].append(row[1])
                        # elif k == 3:
                        #     dict_csv_new["title1"].append(row[0])
                        #     dict_csv_new["href1"].append(row[1])
                        #     dict_csv_new["title2"].append(row[2])
                        # elif k == 4:
                        #     dict_csv_new["title1"].append(row[0])
                        #     dict_csv_new["href1"].append(row[1])
                        #     dict_csv_new["title2"].append(row[2])
                        #     dict_csv_new["href2"].append(row[3])
                        # elif k == 5:
                        #     dict_csv_new["title1"].append(row[0])
                        #     dict_csv_new["href1"].append(row[1])
                        #     dict_csv_new["title2"].append(row[2])
                        #     dict_csv_new["href2"].append(row[3])
                        #     dict_csv_new["title3"].append(row[4])
                        # elif k == 6:
                        #     dict_csv_new["title1"].append(row[0])
                        #     dict_csv_new["href1"].append(row[1])
                        #     dict_csv_new["title2"].append(row[2])
                        #     dict_csv_new["href2"].append(row[3])
                        #     dict_csv_new["title3"].append(row[4])
                        #     dict_csv_new["href3"].append(row[5])
                        # elif k == 7:
                        #     dict_csv_new["title1"].append(row[0])
                        #     dict_csv_new["href1"].append(row[1])
                        #     dict_csv_new["title2"].append(row[2])
                        #     dict_csv_new["href2"].append(row[3])
                        #     dict_csv_new["title3"].append(row[4])
                        #     dict_csv_new["href3"].append(row[5])
                        #     dict_csv_new["title4"].append(row[6])
                        # elif k == 8:
                        #     dict_csv_new["title1"].append(row[0])
                        #     dict_csv_new["href1"].append(row[1])
                        #     dict_csv_new["title2"].append(row[2])
                        #     dict_csv_new["href2"].append(row[3])
                        #     dict_csv_new["title3"].append(row[4])
                        #     dict_csv_new["href3"].append(row[5])
                        #     dict_csv_new["title4"].append(row[6])
                        #     dict_csv_new["href4"].append(row[7])
                        # elif k == 9:
                        #     dict_csv_new["title1"].append(row[0])
                        #     dict_csv_new["href1"].append(row[1])
                        #     dict_csv_new["title2"].append(row[2])
                        #     dict_csv_new["href2"].append(row[3])
                        #     dict_csv_new["title3"].append(row[4])
                        #     dict_csv_new["href3"].append(row[5])
                        #     dict_csv_new["title4"].append(row[6])
                        #     dict_csv_new["href4"].append(row[7])
                        #     dict_csv_new["name"].append(row[8])
                        # elif k == 10:
                        #     dict_csv_new["title1"].append(row[0])
                        #     dict_csv_new["href1"].append(row[1])
                        #     dict_csv_new["title2"].append(row[2])
                        #     dict_csv_new["href2"].append(row[3])
                        #     dict_csv_new["title3"].append(row[4])
                        #     dict_csv_new["href3"].append(row[5])
                        #     dict_csv_new["title4"].append(row[6])
                        #     dict_csv_new["href4"].append(row[7])
                        #     dict_csv_new["name"].append(row[8])
                        #     dict_csv_new["tel1"].append(row[9])
                        # elif k > 10:
                        #     dict_csv_new["title1"].append(row[0])
                        #     dict_csv_new["href1"].append(row[1])
                        #     dict_csv_new["title2"].append(row[2])
                        #     dict_csv_new["href2"].append(row[3])
                        #     dict_csv_new["title3"].append(row[4])
                        #     dict_csv_new["href3"].append(row[5])
                        #     dict_csv_new["title4"].append(row[6])
                        #     dict_csv_new["href4"].append(row[7])
                        #     dict_csv_new["name"].append(row[8])
                        #     dict_csv_new["tel1"].append(row[9])
                        #     dict_csv_new["tel2"].append(row[10])
                    except Exception as e:
                        print("Ошибка при работе чтение строки"
                              "из файла:", e)
                        logger.error("Ошибка при работе чтение строки из файла "
                                     "%file_name: %e", file_name, e)
                        # logger.error("Ошибка при работе чтение строки"
                        #              "из файла {file_name}: "
                        #              "{e}".format(e=e, file_name=file_name))
                count += 1
            print(f'Всего в файле {count} строк.')
            # logger.warning('Всего в файле {count} строк.'.format(count=count))
            logger.warning('Всего в файле %count строк.', count)
    except Exception as e:
        print("Ошибка при работе с файлом:", e)
        logger.error("Ошибка при работе чтение строки из файла "
                      "%file_name: %e", file_name, e)
        # logger.error("Ошибка при работе чтение строки"
        #              "из файла {file_name}: "
        #              "{e}".format(e=e, file_name=file_name))
    return dict_csv_new


def writer_csv(export_data, file_name=""):
    try:
        file_name = file_name + ".csv"
        # Запись в файл
        with open(file_name, 'w', encoding='windows-1251',
                  newline="") as csv_file:
            # Создаем объект writer, указываем символ-разделитель ";"
            writer = csv.writer(csv_file, dialect='excel', delimiter=';', quoting=csv.QUOTE_ALL)
            # Запись данных строки, содержащей заголовки для столбцов в CSV файла
            writer.writerow(("item_1", "item_2", "item_3", "item_4", "item_5",
                             "item_6", "item_7", "item_8", "item_9", "item_10", "item_11"))
            # Запись данных в CSV файла
            writer.writerows(export_data)
            # logger.info('Vse horosho, zapisan file: {file_name}'.format(file_name=file_name))
    except Exception as e:
        print("Ошибка при работе с файлом:", e)
        logger.error("Ошибка при работе чтение строки из файла "
                     "%file_name: %e", file_name, e)
        # logger.error("Ошибка при работе чтение строки"
        #              "из файла {file_name}: "
        #              "{e}".format(e=e, file_name=file_name))


if __name__ == "__main__":
    pass

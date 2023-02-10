import time
import pandas as pd

import app_logger
import dict_new
import list_parse
# import package1
import text_replace
import vremy


logger = app_logger.get_logger(__name__)


def main():
    start = time.time()
    # logger.info("Программа стартует")
    # package1.process(msg="сообщение")
    # logger.warning("Это должно появиться как в консоли, так и в файле журнала")
    url = "https://perevozka24.ru/arenda-spetstehniki"
    region1 = list_parse.list_links(url, "a", "class", "region_link_href", 1)
    del url

    df = pd.DataFrame(region1)
    del region1

    df.to_csv("pandas0001.csv", sep=';', encoding='utf-8-sig', index=False)
    # df.to_excel("pandas0001.xls")
    # df.to_excel("pandas0001.xlsx")
    df.to_json("pandas0001.json", orient='index')
    # df.to_xml("pandas0001.xml")

    # newcsv = pd.read_csv("pandas0001.csv", sep=';')
    # print("csv: ", newcsv)
    # newjson = pd.read_json("pandas0001.json", orient='index')
    # print("json: ", newjson)

    logger.warning('Vse horosho, shag 1, zakonchilsia: {vremy_now}'.format(vremy_now=vremy.vremy_now(start)))

    city_new = dict_new.dict_new(2)
    len1 = len(df.index)
    n = 1
    for i, row in df.iterrows():
        city = list_parse.list_links(row[1], "a", "class", "region_link", 2, row[0])
        len_city_href2 = len(city["href2"])
        for j in range(len_city_href2):
            title1 = row[0]
            href1 = row[1]
            city_new["title1"].append(title1)
            city_new["href1"].append(href1)
            title2 = city["title2"][j]
            href2 = city["href2"][j]
            city_new["title2"].append(title2)
            city_new["href2"].append(href2)

        city_df = pd.DataFrame(city_new)

        city_df.to_csv("pandas0002.csv", sep=';', encoding='utf-8-sig', index=False)
        # city_df.to_excel("pandas0002.xls")
        # city_df.to_excel("pandas0002.xlsx")
        city_df.to_json("pandas0002.json", orient='index')
        # city_df.to_xml("pandas0002.xml")

        # newcsv = pd.read_csv("pandas0002.csv", sep=';')
        # print("csv: ", newcsv)
        # newjson = pd.read_json("pandas0002.json", orient='index')
        # print("json: ", newjson)

        print("i:", n, " iz ", len1, "   ", n / len1 * 100, "prochentov, shag 2 iz 5")
        n += 1

    del df
    del city_new
    del n
    del len1

    logger.warning('Vse horosho, shag 2, zakonchilsia: {vremy_now}'.format(vremy_now=vremy.vremy_now(start)))

    spec_new = dict_new.dict_new(3)
    len2 = len(city_df.index)
    n = 1
    for i, row in city_df.iterrows():
        spec = list_parse.list_links(row[3], "div", "class", "show_group", 3, row[2])
        len_spec_href3 = len(spec["href3"])
        for j in range(len_spec_href3):
            title1 = row[0]
            href1 = row[1]
            spec_new["title1"].append(title1)
            spec_new["href1"].append(href1)
            title2 = row[2]
            href2 = row[3]
            spec_new["title2"].append(title2)
            spec_new["href2"].append(href2)
            title3 = spec["title3"][j]
            href3 = spec["href3"][j]
            spec_new["title3"].append(title3)
            spec_new["href3"].append(href3)

        spec_df = pd.DataFrame(spec_new)

        spec_df.to_csv("pandas0003.csv", sep=';', encoding='utf-8-sig', index=False)
        # city_df.to_excel("pandas0003.xls")
        # city_df.to_excel("pandas0003.xlsx")
        spec_df.to_json("pandas0003.json", orient='index')
        # city_df.to_xml("pandas0003.xml")

        # newcsv = pd.read_csv("pandas0003.csv", sep=';')
        # print("csv: ", newcsv)
        # newjson = pd.read_json("pandas0003.json", orient='index')
        # print("json: ", newjson)

        print("i:", n, " iz ", len2, "   ", n / len2 * 100, "prochentov, shag 3 iz 5")
        n += 1

    del df
    del spec_new
    del n
    del len2
    logger.warning('Vse horosho, shag 3, zakonchilsia: {vremy_now}'.format(vremy_now=vremy.vremy_now(start)))

    del spec_df


if __name__ == "__main__":
    main()

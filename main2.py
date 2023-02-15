import pandas as pd

import app_logger
import dict_new
import list_parse
# import package1
import text_replace
import vremy


logger = app_logger.get_logger(__name__)


def main():
    start = vremy.time.time()
    # logger.info("Программа стартует")
    # package1.process(msg="сообщение")
    # logger.warning("Это должно появиться как в консоли, так и в файле журнала")
    url = "https://perevozka24.ru/arenda-spetstehniki"
    STEP = 10
    kolzapros = 0
    region1 = list_parse.list_links(url, "a", "class", "region_link_href", 1, kolzapros, STEP)
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

    logger.warning('Vse horosho, shag 1,'
                   'zakonchilsia: {vremy_now}'.format(vremy_now=vremy.vremy_now(start)))
    # vremy_now = vremy.vremy_now(start)
    # logger.warning('Vse horosho, shag 1, zakonchilsia: %vremy_now', vremy_now)   

    city_new = dict_new.dict_new(2)
    len1 = len(df.index)
    for i, row in df.iterrows():
        vremy.vremy_now(start)
        city = list_parse.list_links(row[1], "a", "class", "region_link",
                                     2, kolzapros, STEP, row[0])
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

        print("i:", (i+1), " iz ", len1, "   ", (i+1) / len1 * 100, "prochentov, shag 2 iz 5")

    del df
    del city_new
    # del i
    del len1

    logger.warning('Vse horosho, shag 2,'
                   'zakonchilsia: {vremy_now}'.format(vremy_now=vremy.vremy_now(start)))
    # vremy_now = vremy.vremy_now(start)
    # logger.warning('Vse horosho, shag 2, zakonchilsia: %vremy_now', vremy_now)   

    spec_new = dict_new.dict_new(3)
    len2 = len(city_df.index)
    for i, row in city_df.iterrows():
        vremy.vremy_now(start)
        spec = list_parse.list_links(row[3], "div", "class", "show_group",
                                     3, kolzapros, STEP, row[2])
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
        # spec_df.to_excel("pandas0003.xls")
        # spec_df.to_excel("pandas0003.xlsx")
        spec_df.to_json("pandas0003.json", orient='index')
        # spec_df.to_xml("pandas0003.xml")

        # newcsv = pd.read_csv("pandas0003.csv", sep=';')
        # print("csv: ", newcsv)
        # newjson = pd.read_json("pandas0003.json", orient='index')
        # print("json: ", newjson)

        print("i:", (i+1), " iz ", len2, "   ", (i+1) / len2 * 100, "prochentov, shag 3 iz 5")

    del city_df
    del spec_new
    # del i
    del len2
    logger.warning('Vse horosho, shag 3,'
                   'zakonchilsia: {vremy_now}'.format(vremy_now=vremy.vremy_now(start)))
    # vremy_now = vremy.vremy_now(start)
    # logger.warning('Vse horosho, shag 3, zakonchilsia: %vremy_now', vremy_now)   

    prolog_new = dict_new.dict_new(4)
    len3 = len(spec_df.index)
    for i, row in spec_df.iterrows():
        vremy.vremy_now(start)
        prolog = list_parse.list_links(row[5], "ul", "class",
                                       "pagination pages-pagination inline-block",
                                       4, kolzapros, STEP, row[4])
        len_prolog_href4 = len(prolog["href4"])
        for j in range(len_prolog_href4):
            title1 = row[0]
        href1 = row[1]
        prolog_new["title1"].append(title1)
        prolog_new["href1"].append(href1)
        title2 = row[2]
        href2 = row[3]
        prolog_new["title2"].append(title2)
        prolog_new["href2"].append(href2)
        title3 = row[4]
        href3 = row[5]
        prolog_new["title3"].append(title3)
        prolog_new["href3"].append(href3)
        title4 = prolog["title4"][j]
        href4 = prolog["href4"][j]
        prolog_new["title4"].append(title4)
        prolog_new["href4"].append(href4)

    prolog_df = pd.DataFrame(prolog_new)

    prolog_df.to_csv("pandas0004.csv", sep=';', encoding='utf-8-sig', index=False)
    # prolog_df.to_excel("pandas0004.xls")
    # prolog_df.to_excel("pandas0004.xlsx")
    prolog_df.to_json("pandas0004.json", orient='index')
    # prolog_df.to_xml("pandas0004.xml")

    # newcsv = pd.read_csv("pandas0004.csv", sep=';')
    # print("csv: ", newcsv)
    # newjson = pd.read_json("pandas0004.json", orient='index')
    # print("json: ", newjson)

    print("i:", (i+1), " iz ", len3, "   ", (i+1) / len3 * 100, "prochentov, shag 4 iz 5")

    del spec_df
    del prolog_new
    # del i
    del len3
    logger.warning('Vse horosho, shag 4,'
                   'zakonchilsia: {vremy_now}'.format(vremy_now=vremy.vremy_now(start)))
    # vremy_now = vremy.vremy_now(start)
    # logger.warning('Vse horosho, shag 4, zakonchilsia: %vremy_now', vremy_now)   
    telephone_new = dict_new.dict_new(5)
    len4 = len(prolog_df.index)
    for i, row in prolog_df.iterrows():
        vremy.vremy_now(start)
        telephone = list_parse.list_links_tel(row[7], "div", "class", "cb-inner",
                                              "cb-name", "cb-data", kolzapros, STEP)
        if telephone is not None:
            len_telephone_name = len(telephone["name"])
            for j in range(len_telephone_name):
                title1 = text_replace.link_replace(row[0])
                href1 = text_replace.link_replace(row[1])
                telephone_new["title1"].append(title1)
                telephone_new["href1"].append(href1)
                title2 = text_replace.link_replace(row[2])
                href2 = text_replace.link_replace(row[3])
                telephone_new["title2"].append(title2)
                telephone_new["href2"].append(href2)
                title3 = text_replace.link_replace(row[4])
                href3 = text_replace.link_replace(row[5])
                telephone_new["title3"].append(title3)
                telephone_new["href3"].append(href3)
                title4 = text_replace.link_replace(row[6])
                href4 = text_replace.link_replace(row[7])
                telephone_new["title4"].append(title4)
                telephone_new["href4"].append(href4)
                name5_replace = text_replace.link_replace(telephone["name"][j])
                name5 = text_replace.link_replase_tel_name(name5_replace)
                tel51_replace = text_replace.link_replace_tel(telephone["tel1"][j])
                tel51 = text_replace.link_replase_tel_number(tel51_replace)
                tel52 = text_replace.link_replace_tel(telephone["tel2"][j])
                telephone_new["name"].append(name5)
                telephone_new["tel1"].append(tel51)
                telephone_new["tel2"].append(tel52)

        telephone_df = pd.DataFrame(telephone_new)

        telephone_df.to_csv("pandas0005.csv", sep=';', encoding='utf-8-sig', index=False)
        # telephone_df.to_excel("pandas0005.xls")
        # telephone_df.to_excel("pandas0005.xlsx")
        telephone_df.to_json("pandas0005.json", orient='index')
        # telephone_df.to_xml("pandas0005.xml")

        # newcsv = pd.read_csv("pandas0005.csv", sep=';')
        # print("csv: ", newcsv)
        # newjson = pd.read_json("pandas0005.json", orient='index')
        # print("json: ", newjson)

        print("i:", (i+1), " iz ", len4, "   ", (i+1) / len4 * 100, "prochentov, shag 5 iz 5")

    del prolog_df
    del telephone_new
    # del i
    del len4
    logger.warning('Vse horosho, shag 5,'
                   'zakonchilsia: {vremy_now}'.format(vremy_now=vremy.vremy_now(start)))
    # vremy_now = vremy.vremy_now(start)
    # logger.warning('Vse horosho, shag 5, zakonchilsia: %vremy_now', vremy_now)   

    del telephone_df
    del STEP
    del kolzapros

    # logger.info("Программа завершила работу")


if __name__ == "__main__":
    main()

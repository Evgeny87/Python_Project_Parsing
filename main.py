from itertools import zip_longest

import app_logger
import csv_rw
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
    item_1 = region1["title1"]
    item_2 = region1["href1"]
    data = [item_1, item_2]
    export_data = zip_longest(*data, fillvalue="")
    csv_rw.writer_csv(export_data, "dict0001")
    logger.warning('Vse horosho, shag 1,'
                   'zakonchilsia: {vremy_now}'.format(vremy_now=vremy.vremy_now(start)))
    # vremy_now = vremy.vremy_now(start)
    # logger.warning('Vse horosho, shag 1, zakonchilsia: %vremy_now', vremy_now)   
    city_new = dict_new.dict_new(2)
    len_region_href1 = len(region1["href1"])
    for i in range(len_region_href1):
        a = i + 1
        len1 = len_region_href1 + 1
        print("i:", a, " iz ", len1, "   ", a / len1 * 100, "prochentov, shag 2 iz 5")
        vremy.vremy_now(start)
        city = list_parse.list_links(region1["href1"][i], "a", "class","region_link",
                                     2, kolzapros, STEP, region1["title1"][i])
        len_city_href2 = len(city["href2"])
        for j in range(len_city_href2):
            title1 = region1["title1"][i]
            href1 = region1["href1"][i]
            city_new["title1"].append(title1)
            city_new["href1"].append(href1)
            title2 = city["title2"][j]
            href2 = city["href2"][j]
            city_new["title2"].append(title2)
            city_new["href2"].append(href2)
        item_1 = city_new["title1"]
        item_2 = city_new["href1"]
        item_3 = city_new["title2"]
        item_4 = city_new["href2"]
        data = [item_1, item_2, item_3, item_4]
        export_data = zip_longest(*data, fillvalue="")
        csv_rw.writer_csv(export_data, "dict0002")
    # logger.warning('Vse horosho, shag 2,'
    #                'zakonchilsia: {vremy_now}'.format(vremy_now=vremy.vremy_now(start)))
    logger.warning('Vse horosho, shag 2,'
                   'zakonchilsia: %vremy_now', vremy.vremy_now(start))
    spec_new = dict_new.dict_new(3)
    len_citynew_href2 = len(city_new["href2"])
    for i in range(len_citynew_href2):
        b = i + 1
        len2 = len_citynew_href2 + 1
        print("i:", b, " iz ", len2, "   ", b / len2 * 100, "prochentov, shag 3 iz 5")
        vremy.vremy_now(start)
        spec = list_parse.list_links(city_new["href2"][i], "div", "class", "show_group",
                                     3, kolzapros, STEP, city_new["title2"][i])
        len_spec_href3 = len(spec["href3"])
        for j in range(len_spec_href3):
            title1 = city_new["title1"][i]
            href1 = city_new["href1"][i]
            spec_new["title1"].append(title1)
            spec_new["href1"].append(href1)
            title2 = city_new["title2"][i]
            href2 = city_new["href2"][i]
            spec_new["title2"].append(title2)
            spec_new["href2"].append(href2)
            title3 = spec["title3"][j]
            href3 = spec["href3"][j]
            spec_new["title3"].append(title3)
            spec_new["href3"].append(href3)
        item_1 = spec_new["title1"]
        item_2 = spec_new["href1"]
        item_3 = spec_new["title2"]
        item_4 = spec_new["href2"]
        item_5 = spec_new["title3"]
        item_6 = spec_new["href3"]
        data = [item_1, item_2, item_3, item_4, item_5, item_6]
        export_data = zip_longest(*data, fillvalue="")
        csv_rw.writer_csv(export_data, "dict0003")
    # logger.warning('Vse horosho, shag 3,'
    #                'zakonchilsia: {vremy_now}'.format(vremy_now=vremy.vremy_now(start)))
    logger.warning('Vse horosho, shag 3,'
                   'zakonchilsia: %vremy_now', vremy.vremy_now(start))
    prolog_new = dict_new.dict_new(4)
    len_specnew_href3 = len(spec_new["href3"])
    for i in range(len_specnew_href3):
        c = i + 1
        len3 = len_specnew_href3 + 1
        print("i:", c, " iz ", len3, "   ", c / len3 * 100, "prochentov, shag 4 iz 5")
        vremy.vremy_now(start)
        prolog = list_parse.list_links(spec_new["href3"][i], "ul", "class",
                                       "pagination pages-pagination inline-block",
                                       4, kolzapros, STEP, spec_new["title3"][i])
        len_prolog_href4 = len(prolog["href4"])
        for j in range(len_prolog_href4):
            title1 = spec_new["title1"][i]
            href1 = spec_new["href1"][i]
            prolog_new["title1"].append(title1)
            prolog_new["href1"].append(href1)
            title2 = spec_new["title2"][i]
            href2 = spec_new["href2"][i]
            prolog_new["title2"].append(title2)
            prolog_new["href2"].append(href2)
            title3 = spec_new["title3"][i]
            href3 = spec_new["href3"][i]
            prolog_new["title3"].append(title3)
            prolog_new["href3"].append(href3)
            title4 = prolog["title4"][j]
            href4 = prolog["href4"][j]
            prolog_new["title4"].append(title4)
            prolog_new["href4"].append(href4)
        item_1 = prolog_new["title1"]
        item_2 = prolog_new["href1"]
        item_3 = prolog_new["title2"]
        item_4 = prolog_new["href2"]
        item_5 = prolog_new["title3"]
        item_6 = prolog_new["href3"]
        item_7 = prolog_new["title4"]
        item_8 = prolog_new["href4"]
        data = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8]
        export_data = zip_longest(*data, fillvalue="")
        csv_rw.writer_csv(export_data, "dict0004")
    # logger.warning('Vse horosho, shag 4,'
    #                'zakonchilsia: {vremy_now}'.format(vremy_now=vremy.vremy_now(start)))
    logger.warning('Vse horosho, shag 4,'
                   'zakonchilsia: %vremy_now', vremy.vremy_now(start))
    telephone_new = dict_new.dict_new(5)
    len_prolog_href4 = len(prolog_new["href4"])
    for i in range(len_prolog_href4):
        c = i + 1
        len4 = len_prolog_href4 + 1
        print("i:", c, " iz ", len4, "   ", c / len4 * 100, "prochentov, shag 5 iz 5")
        vremy.vremy_now(start)
        telephone = list_parse.list_links_tel(prolog_new["href4"][i], "div", "class",
                                              "cb-inner", "cb-name", "cb-data",
                                              kolzapros, STEP)
        print("prolog_new[href4][", i, "]: ", prolog_new["href4"][i])
        if telephone is not None:
            len_telephone_name = len(telephone["name"])
            for j in range(len_telephone_name):
                title1 = text_replace.link_replace(prolog_new["title1"][i])
                href1 = text_replace.link_replace(prolog_new["href1"][i])
                telephone_new["title1"].append(title1)
                telephone_new["href1"].append(href1)
                title2 = text_replace.link_replace(prolog_new["title2"][i])
                href2 = text_replace.link_replace(prolog_new["href2"][i])
                telephone_new["title2"].append(title2)
                telephone_new["href2"].append(href2)
                title3 = text_replace.link_replace(prolog_new["title3"][i])
                href3 = text_replace.link_replace(prolog_new["href3"][i])
                telephone_new["title3"].append(title3)
                telephone_new["href3"].append(href3)
                title4 = text_replace.link_replace(prolog_new["title4"][i])
                href4 = text_replace.link_replace(prolog_new["href4"][i])
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
        item_1 = telephone_new["title1"]
        item_2 = telephone_new["href1"]
        item_3 = telephone_new["title2"]
        item_4 = telephone_new["href2"]
        item_5 = telephone_new["title3"]
        item_6 = telephone_new["href3"]
        item_7 = telephone_new["title4"]
        item_8 = telephone_new["href4"]
        item_9 = telephone_new["name"]
        item_10 = telephone_new["tel1"]
        item_11 = telephone_new["tel2"]
        data = [item_1, item_2, item_3, item_4, item_5, item_6,
                item_7, item_8, item_9, item_10, item_11]
        export_data = zip_longest(*data, fillvalue="")
        csv_rw.writer_csv(export_data, "dict0005")
    # logger.warning('Vse horosho, shag 5,'
    #                'zakonchilsia: {vremy_now}'.format(vremy_now=vremy.vremy_now(start)))
    logger.warning('Vse horosho, shag 5,'
                   'zakonchilsia: %vremy_now', vremy.vremy_now(start))
    # logger.info("Программа завершила работу")


if __name__ == "__main__":
    main()

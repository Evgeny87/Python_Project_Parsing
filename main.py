import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import csv_rw
from itertools import zip_longest
# import package1
import app_logger
import re


logger = app_logger.get_logger(__name__)


def url_to_parse(url_site=""):
    for i in range(100):
        ua = UserAgent(verify_ssl=False)
        us_ag = ua.random
        ua = us_ag.strip()
        headers = {'Content-Type': 'text/html', 'accept': '*/*', 'user-agent': ua}
        response = requests.get(url_site, headers=headers, timeout=None)
        # print(response.encoding)
        # response.encoding = 'utf-8'
        # response.content.decode('utf-8')
        try:
            response.raise_for_status()
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
            print("Ошибка timeout, url:", url_site)
            logger.error("Timeout Error: {errt}".format(errt=errt))
            logger.error("Ошибка timeout, url: {url_site}".format(url_site=url_site))
        except requests.exceptions.ReadTimeout as errrt:
            print("ReadTimeout Error:", errrt)
            logger.error("ReadTimeout Error: {errrt}, url: {url_site}".format(errrt=errrt, url_site=url_site))
        except requests.exceptions.ConnectTimeout as errct:
            print("ConnectTimeout Error:", errct)
            logger.error("ConnectTimeout Error: {errct}, url: {url_site}".format(errct=errct, url_site=url_site))
        except requests.exceptions.TooManyRedirects as errtmr:
            print("TooManyRedirects Error:", errtmr)
            logger.error("TooManyRedirects Error: {errtmr}, url: {url_site}".format(errtmr=errtmr, url_site=url_site))
        except requests.exceptions.URLRequired as errur:
            print("URLRequired Error:", errur)
            logger.error("URLRequired Error: {errur}, url: {url_site}".format(errur=errur, url_site=url_site))
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
            code = errh.response.status_code
            print("Ошибка url: {0}, code: {1}".format(url_site, code))
            print("Connection Error: ", response.status_code)
            logger.error("Http Error: {errh}".format(errh=errh))
            logger.error("Ошибка url: {url_site}, code: {code}".format(url_site=url_site, code=code))
            logger.error("Connection Error: {status_code}".format(status_code=response.status_code))
            if code == 404:
                soup = BeautifulSoup(response.text, "html.parser")
                # logger.info('Vse ploho 404 oshibka')
                break
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
            logger.error("Error Connecting: {errc}, url: {url_site}".format(errc=errc, url_site=url_site))
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
            print("Ошибка скачивания url: ", url_site)
            logger.error("OOps: Something Else: {err}".format(err=err))
            logger.error("Ошибка скачивания url: {url_site}".format(url_site=url_site))
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            # soup = BeautifulSoup(response.content, "html.parser")
            # logger.info('Vse horosho soup gotov')
            break
        print("Oshibka: ", i+1)
        logger.error("Oshibka: {i}, url: {url_site}".format(i=i+1, url_site=url_site))
        time.sleep(i+1)
    else:
        print("Poproboval 10 raz otpravit")
        logger.error("Poproboval 10 raz otpravit, url: {url_site}".format(url_site=url_site))
    return soup, response.status_code


def link_replace(link):
    link = link.strip()
    while "  " in link:
        link = link.replace("\r", "")
        link = link.replace("\n", "")
        # link = link.replace('\xeb', 'е')
        link = link.replace("  ", " ")
    link = link.strip()
    return link


def link_replace_tel(link):
    link = link.strip()
    while "  " in link:
        link = link.replace("\r", "")
        link = link.replace("\n", "")
        # link = link.replace('\u2212', '-')
        # link = link.replace('\xeb', 'е')
        link = link.replace("-", "")
        link = link.replace("(", "")
        link = link.replace(")", "")
        link = link.replace("  ", "")
        link = link.replace(" ", "")
        link = link.replace("+7", "8")
    link = link.strip()
    return link


def list_links(url_site="", teg1="", selector="", name="", lvl=0, title_ishod=""):
    url_ishod = url_site
    soup, code = url_to_parse(url_site)
    url_site = soup
    k = 1
    if code != 200:
        pass
    else:
        links = url_site.find_all(teg1, {selector: name})
        lvl_max = lvl + 1
        result_list = dict()
        for i in range(1, lvl_max):
            title_i = "title" + str(i)
            href_i = "href" + str(i)
            key, value = title_i, []
            result_list[key] = value
            key, value = href_i, []
            result_list[key] = value
        title = 'title' + str(lvl)
        href = 'href' + str(lvl)
        if links == []:
            if lvl == 4:
                result_list[href].append(url_ishod)
                result_list[title].append("1")
                for i in range(2, 100):
                    url_site_code = str(url_ishod + "/" + str(i))
                    soup, code = url_to_parse(url_site_code)
                    if code != 200:
                        break
                    else:
                        result_list[href].append(url_site_code)
                        result_list[title].append(i)
            else:
                result_list[title].append(title_ishod)
                result_list[href].append(url_ishod)
        else:
            for link in links:
                if lvl == 3:
                    abc = link.find("a")
                elif lvl == 4:
                    abc = link.find_all("a")
                    result_list[href].append(url_ishod)
                    result_list[title].append("1")
                else:
                    abc = link
                if abc is not None:
                    if lvl == 4:
                        for ab in abc:
                            result_list[href].append(ab.get("href"))
                            link = link_replace(ab.text)
                            result_list[title].append(link)
                            k += 1
                        for i in range(k+1, 100):
                            url_site_code = str(url_ishod + "/" + str(i))
                            soup, code = url_to_parse(url_site_code)
                            if code != 200:
                                break
                            else:
                                result_list[href].append(ab.get("href"))
                                link = link_replace(ab.text)
                                result_list[title].append(link)
                    else:
                        result_list[href].append('https://perevozka24.ru' + abc.get("href"))
                        link = link_replace(abc.text)
                        result_list[title].append(link)
        return result_list


def list_links_tel(url_site="", teg="", selector="", name1="", name2="", name3=""):
    soup, code = url_to_parse(url_site)
    url_site = soup
    if code != 200:
        pass
    else:
        links1 = url_site.find_all(teg, {selector: name1})
        result_list = dict()
        name = "name"
        key, value = name, []
        result_list[key] = value
        tel1 = "tel1"
        key, value = tel1, []
        result_list[key] = value
        tel2 = "tel2"
        key, value = tel2, []
        result_list[key] = value
        for link in links1:
            links2 = link.find(teg, {selector: name2})
            links2 = links2.text
            if str(links2).split("\n", 2)[1] != "":
                links2 = str(links2).split("\n", 2)[1]
            else:
                links2 = str(links2).split("\n\n", 2)[1]
            links2 = link_replace(links2)
            links3 = link.find(teg, {selector: name3})
            tel_tel = links3.find_all('span', {"class": 'javalnk'})
            tel_tel = (link_replace_tel(str(tel_tel)).split(','))
            for elem_tel in tel_tel:
                elem_tel = re.split('<|>', elem_tel)
                if elem_tel[0] != "[]":
                    if link_replace(elem_tel[2]) != "WhatsApp":
                        tel10 = link_replace_tel(elem_tel[2])
                        result_list[name].append(links2)
                        result_list[tel1].append(tel10)
                        result_list[tel2].append("telefon")
            tel_whatsapp = links3.find_all('span', {"class": 'whatsapp-btn javalnk blank'})
            tel_whatsapp = link_replace_tel(str(tel_whatsapp)).split(',')
            for elem_whatsapp in tel_whatsapp:
                elem_whatsapp = re.split('/|">', elem_whatsapp)
                if elem_whatsapp[0] != "[]":
                    if elem_whatsapp[3] != None:
                        tel10 = link_replace_tel("+" + elem_whatsapp[3])
                        tel10 = tel10.replace("+7", "8")
                        result_list[name].append(links2)
                        result_list[tel1].append(tel10)
                        result_list[tel2].append("whatsapp")
            tel_viber = links3.find_all('a', {"class": 'viber-btn'})
            tel_viber = link_replace_tel(str(tel_viber)).split(',')
            for elem_viber in tel_viber:
                elem_viber = re.split('"|B', elem_viber)
                if elem_viber[0] != "[]":
                    if elem_viber[3] != None:
                        tel10 = link_replace_tel("+" + elem_viber[4])
                        tel10 = tel10.replace("+7", "8")  
                        result_list[name].append(links2)
                        result_list[tel1].append(tel10)
                        result_list[tel2].append("viber")
        return result_list


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


def convert_to_preferred_format(sec):
    day = sec // 86400
    sec %= 86400
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    sec1 = sec // 1
    dol_sec = sec % 1
    sec = sec1
    # print("seconds value in day: ", day)
    # print("seconds value in hours: ", hour)
    # print("seconds value in minutes: ", min)
    # print("seconds value in seconds: ", sec)
    # print("seconds value in dol_seconds: ", dol_sec)
    return "%01d day, %02d:%02d:%02d, %1.8f" % (day, hour, min, sec, dol_sec)


def vremy_now(start):
    now = time.time()
    raznicha = now - start
    vremia = convert_to_preferred_format(raznicha)
    print(vremia)
    return vremia


def main():
    start = time.time()
    # logger.info("Программа стартует")
    # package1.process(msg="сообщение")
    # logger.warning("Это должно появиться как в консоли, так и в файле журнала")
    region1 = dict_new(1)
    url = "https://perevozka24.ru/arenda-spetstehniki"
    region1 = list_links(url, "a", "class", "region_link_href", 1)
    item_1 = region1["title1"]
    item_2 = region1["href1"]
    data = [item_1, item_2]
    export_data = zip_longest(*data, fillvalue="")
    csv_rw.writer_csv(export_data, "dict0001")
    logger.warning('Vse horosho, shag 1, zakonchilsia: {vremy_now}'.format(vremy_now=vremy_now(start)))
    city_new = dict_new(2)
    len_region_href1 = len(region1["href1"])
    for i in range(len_region_href1):
        a = i + 1
        len1 = len_region_href1 + 1
        print("i:", a, " iz ", len1, "   ", a / len1 * 100, "prochentov, shag 2 iz 5")
        vremy_now(start)
        city = list_links(region1["href1"][i], "a", "class", "region_link", 2, region1["title1"][i])
        for j in range(len(city["href2"])):
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
    logger.warning('Vse horosho, shag 2, zakonchilsia: {vremy_now}'.format(vremy_now=vremy_now(start)))
    spec_new = dict_new(3)
    len_citynew_href2 = len(city_new["href2"])
    for i in range(len_citynew_href2):
        b = i + 1
        len2 = len_citynew_href2 + 1
        print("i:", b, " iz ", len2, "   ", b / len2 * 100, "prochentov, shag 3 iz 5")
        vremy_now(start)
        spec = list_links(city_new["href2"][i], "div", "class", "show_group", 3, city_new["title2"][i])
        for j in range(len(spec["href3"])):
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
    logger.warning('Vse horosho, shag 3, zakonchilsia: {vremy_now}'.format(vremy_now=vremy_now(start)))
    prolog_new = dict_new(4)
    len_specnew_href3 = len(spec_new["href3"])
    for i in range(len_specnew_href3):
        c = i + 1
        len3 = len_specnew_href3 + 1
        print("i:", c, " iz ", len3, "   ", c / len3 * 100, "prochentov, shag 4 iz 5")
        vremy_now(start)
        prolog = list_links(spec_new["href3"][i], "ul", "class", "pagination pages-pagination inline-block", 4, spec_new["title3"][i])
        for j in range(len(prolog["href4"])):
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
    logger.warning('Vse horosho, shag 4, zakonchilsia: {vremy_now}'.format(vremy_now=vremy_now(start)))
    telephone_new = dict_new(5)
    len_prolog_href4 = len(prolog_new["href4"])
    for i in range(len_prolog_href4):
        c = i + 1
        len4 = len_prolog_href4 + 1
        print("i:", c, " iz ", len4, "   ", c / len4 * 100, "prochentov, shag 5 iz 5")
        vremy_now(start)
        telephone = list_links_tel(prolog_new["href4"][i], "div", "class", "cb-inner", "cb-name", "cb-data")
        print("prolog_new[href4][", i, "]: ", prolog_new["href4"][i])
        for j in range(len(telephone["name"])):
            title1 = link_replace(prolog_new["title1"][i])
            href1 = link_replace(prolog_new["href1"][i])
            telephone_new["title1"].append(title1)
            telephone_new["href1"].append(href1)
            title2 = link_replace(prolog_new["title2"][i])
            href2 = link_replace(prolog_new["href2"][i])
            telephone_new["title2"].append(title2)
            telephone_new["href2"].append(href2)
            title3 = link_replace(prolog_new["title3"][i])
            href3 = link_replace(prolog_new["href3"][i])
            telephone_new["title3"].append(title3)
            telephone_new["href3"].append(href3)
            title4 = link_replace(prolog_new["title4"][i])
            href4 = link_replace(prolog_new["href4"][i])
            telephone_new["title4"].append(title4)
            telephone_new["href4"].append(href4)
            name5 = link_replace(telephone["name"][j])
            tel51 = link_replace_tel(telephone["tel1"][j])
            tel52 = link_replace_tel(telephone["tel2"][j])
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
        data = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11]
        export_data = zip_longest(*data, fillvalue="")
        csv_rw.writer_csv(export_data, "dict0005")
    logger.warning('Vse horosho, shag 5, zakonchilsia: {vremy_now}'.format(vremy_now=vremy_now(start)))
    # logger.info("Программа завершила работу")


if __name__ == "__main__":
   main()

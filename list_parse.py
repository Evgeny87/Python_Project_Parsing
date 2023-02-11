import re

import parse_bs4
import text_replace


def list_links(url_site="", teg1="", selector="", name="", lvl=0, kolzapros=0, STEP=0, title_ishod=""):
    url_ishod = url_site
    soup, code = parse_bs4.url_to_parse(url_site, kolzapros, STEP)
    url_site = soup
    k = 1
    if code != 200:
        pass
    else:
        kolzapros += 1
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
                    soup, code = parse_bs4.url_to_parse(url_site_code)
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
                            link = text_replace.link_replace(ab.text)
                            result_list[title].append(link)
                            k += 1
                        for i in range(k+1, 100):
                            url_site_code = str(url_ishod + "/" + str(i))
                            soup, code = parse_bs4.url_to_parse(url_site_code)
                            if code != 200:
                                break
                            else:
                                result_list[href].append(ab.get("href"))
                                link = text_replace.link_replace(ab.text)
                                result_list[title].append(link)
                    else:
                        result_list[href].append('https://perevozka24.ru' + abc.get("href"))
                        link = text_replace.link_replace(abc.text)
                        result_list[title].append(link)
        return result_list


def list_links_tel(url_site="", teg="", selector="", name1="", name2="", name3="", kolzapros=0, STEP=0):
    soup, code = parse_bs4.url_to_parse(url_site, kolzapros, STEP)
    url_site = soup
    if code != 200:
        pass
    else:
        kolzapros += 1
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
            links2 = text_replace.link_replace(links2)
            links3 = link.find(teg, {selector: name3})
            tel_tel = links3.find_all('span', {"class": 'javalnk'})
            tel_tel = (text_replace.link_replace_tel(str(tel_tel)).split(','))
            for elem_tel in tel_tel:
                elem_tel = re.split('<|>', elem_tel)
                if elem_tel[0] != "[]":
                    if text_replace.link_replace(elem_tel[2]) != "WhatsApp":
                        tel10 = text_replace.link_replace_tel(elem_tel[2])
                        result_list[name].append(links2)
                        result_list[tel1].append(tel10)
                        result_list[tel2].append("telefon")
            tel_whatsapp = links3.find_all('span', {"class": 'whatsapp-btn javalnk blank'})
            tel_whatsapp = text_replace.link_replace_tel(str(tel_whatsapp)).split(',')
            for elem_whatsapp in tel_whatsapp:
                elem_whatsapp = re.split('/|">', elem_whatsapp)
                if elem_whatsapp[0] != "[]":
                    if elem_whatsapp[3] != None:
                        tel10 = text_replace.link_replace_tel("+" + elem_whatsapp[3])
                        tel10 = tel10.replace("+7", "8")
                        result_list[name].append(links2)
                        result_list[tel1].append(tel10)
                        result_list[tel2].append("whatsapp")
            tel_viber = links3.find_all('a', {"class": 'viber-btn'})
            tel_viber = text_replace.link_replace_tel(str(tel_viber)).split(',')
            for elem_viber in tel_viber:
                elem_viber = re.split('"|B', elem_viber)
                if elem_viber[0] != "[]":
                    if elem_viber[3] != None:
                        tel10 = text_replace.link_replace_tel("+" + elem_viber[4])
                        tel10 = tel10.replace("+7", "8")
                        result_list[name].append(links2)
                        result_list[tel1].append(tel10)
                        result_list[tel2].append("viber")
        return result_list


if __name__ == "__main__":
    pass

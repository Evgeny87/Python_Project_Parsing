import re


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
        link = link.replace(",", "")
        link = link.replace("  ", "")
        link = link.replace(" ", "")
        link = link.replace("+7", "8")
    link = link.strip()
    return link


def link_replase_tel_number(tel_str=""):
    tel_number = re.sub(r"[^0-9]", "", tel_str)
    tel_number = tel_number.replace(" ", "")
    return (tel_number)


def link_replase_tel_number2(tel_str=""):
    tel_number2 = ""
    tel = re.findall('[0-9]+', tel_str)
    for i in range(len(tel)):
        tel_number2 = tel_number2 + str(tel[i])
    tel_number2 = tel_number2.replace(" ", "")
    return (tel_number2)


def link_replase_tel_name(tel_name_str=""):
    tel_name = re.sub(r"[^a-zA-Zа-яА-Я0-9@.\-“\"«»()*+/|\\?!,;: ]", "", tel_name_str)
    return (tel_name)


if __name__ == "__main__":
    pass

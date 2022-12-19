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
        link = link.replace("  ", "")
        link = link.replace(" ", "")
        link = link.replace("+7", "8")
    link = link.strip()
    return link


def link_replase_tel_number(tel_str=""):
    x = re.sub(r"[^0-9]", "", tel_str)
    x = x.replace(" ", "")
    return (x)


def link_replase_tel_number2(tel_str=""):
    b = ""
    x = re.findall('[0-9]+', tel_str)
    for i in range(len(x)):
        b = b + str(x[i])
    b = b.replace(" ", "")
    return (b)


def link_replase_tel_name(tel_name_str=""):
    x = re.sub(r"[^a-zA-Zа-яА-Я0-9@.\- ]", "", tel_name_str)
    return (x)


if __name__ == "__main__":
    pass

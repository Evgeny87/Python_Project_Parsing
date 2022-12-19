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


if __name__ == "__main__":
    pass

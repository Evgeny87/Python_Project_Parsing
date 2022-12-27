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

import time


def convert_to_preferred_format(sec):
    day = sec // 86400
    sec %= 86400
    hour = sec // 3600
    sec %= 3600
    minut = sec // 60
    sec %= 60
    sec1 = sec // 1
    dol_sec = sec % 1
    sec = sec1
    # print("seconds value in day: ", day)
    # print("seconds value in hours: ", hour)
    # print("seconds value in minutes: ", minut)
    # print("seconds value in seconds: ", sec)
    # print("seconds value in dol_seconds: ", dol_sec)
    # return "%01d day, %02d:%02d:%02d, %1.8f" % (day, hour, minut, sec, dol_sec)
    vremy = "%day %hour:%minut:%sec %dol_sec", day, hour, minut, sec, dol_sec
    return vremy


def vremy_now(start):
    now = time.time()
    raznicha = now - start
    vremia = convert_to_preferred_format(raznicha)
    print(vremia)
    return vremia


if __name__ == "__main__":
    pass

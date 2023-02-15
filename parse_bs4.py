import random
import time
import string
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import app_logger


logger = app_logger.get_logger(__name__)


# https://dev-gang.ru/article/kak-sgenerirovat-sluczainuu-stroku-v-python-wwnl77lvl4/
def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


def random_ua_and_cookies(kol_zapros=0, STEP=0):
    # if kol_zapros == 0 or kol_zapros % STEP == 0:
    ua = UserAgent(verify_ssl=False)
    us_ag = ua.random
    ua = us_ag.strip()
    cookies_random = str(generate_alphanum_random_string(31))
    return ua, cookies_random


def url_to_parse(url_site="", kol_zapros=0, STEP=0):
    i = 0
    while True:
    # for i in range(100):
        ua, cookies_random = random_ua_and_cookies(kol_zapros, STEP)
        headers = {'Content-Type': 'text/html', 'accept': '*/*', 'user-agent': ua}
        cookies = {'perevozka24_session': cookies_random}
        try:
            response = requests.get(url_site, headers=headers, timeout=None, cookies=cookies)
            # print(response.encoding)
            # response.encoding = 'utf-8'
            # response.content.decode('utf-8')
            response.raise_for_status()
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
            print("Ошибка timeout, url:", url_site)
            # logger.error("Timeout Error: {errt}".format(errt=errt))
            # logger.error("Ошибка timeout, url: {url_site}".format(url_site=url_site))
            logger.error("Timeout Error: %errt", errt)
            logger.error("Ошибка timeout, url: %url_site", url_site) 
        except requests.exceptions.ReadTimeout as errrt:
            print("ReadTimeout Error:", errrt)
            logger.error("ReadTimeout Error: {errrt}, url: {url_site}".format(errrt=errrt,
                                                                              url_site=url_site))
        # except requests.exceptions.ConnectTimeout as errct:
        #     print("ConnectTimeout Error:", errct)
        #     logger.error("ConnectTimeout Error: {errct},"
        #                  "url: {url_site}".format(errct=errct,
        #                  url_site=url_site))
        # except requests.exceptions.TooManyRedirects as errtmr:
        #    print("TooManyRedirects Error:", errtmr)
        #     logger.error("TooManyRedirects Error: {errtmr},"
        #                  "url: {url_site}".format(errtmr=errtmr,
        #                                           url_site=url_site))
            logger.error("TooManyRedirects Error: %errtmr, url: %url_site", errtmr, url_site)
        except requests.exceptions.URLRequired as errur:
            print("URLRequired Error:", errur)
            # logger.error("URLRequired Error: {errur}, url: {url_site}".format(errur=errur,
            #                                                                   url_site=url_site))
            logger.error("URLRequired Error: %errur, url: %url_site", errur, url_site)            
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
            code = errh.response.status_code
            # print("Ошибка url: {0}, code: {1}".format(url_site, code))
            print("Ошибка url: %url_site, code: %code", url_site, code)
            print("Connection Error: ", response.status_code)
            # logger.error("Http Error: {errh}".format(errh=errh))
            # logger.error("Ошибка url: {url_site}, code: {code}".format(url_site=url_site,
            #                                                            code=code))
            # logger.error("Connection Error: " 
            #              "{status_code}".format(status_code=response.status_code))
            
            logger.error("Http Error: %errh", errh)
            logger.error("Ошибка url: %url_site, code: %code", url_site, code)
            # logger.error("Connection Error: %status_code", status_code)
            logger.error("Connection Error: %status_code", response.status_code)
            
            if code == 404:
                soup = BeautifulSoup(response.text, "html.parser")
                # logger.info('Vse ploho 404 oshibka')
                break
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
            # logger.error("Error Connecting: {errc}, url: {url_site}".format(errc=errc,
            #                                                                 url_site=url_site))
            logger.error("Error Connecting: %errc, url: %url_site", errc, url_site)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
            print("Ошибка скачивания url: ", url_site)
            # logger.error("OOps: Something Else: {err}".format(err=err))
            # logger.error("Ошибка скачивания url: {url_site}".format(url_site=url_site))
            logger.error("OOps: Something Else: %err", err)
            logger.error("Ошибка скачивания url: %url_site", url_site)
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            # soup = BeautifulSoup(response.content, "html.parser")
            # logger.info('Vse horosho soup gotov')
            break
        j = i + 1
        print("Oshibka: ", j)
        # logger.error("Oshibka: {i}, url: {url_site}".format(i=i+1, url_site=url_site))
        logger.error("Oshibka: %j, url: %url_site", j, url_site)
        time.sleep(j)
        i += 1
    # else:
    #     print("Poproboval 10 raz otpravit")
    #     logger.error("Poproboval 10 raz otpravit, url: {url_site}".format(url_site=url_site))
    return soup, response.status_code


if __name__ == "__main__":
    pass

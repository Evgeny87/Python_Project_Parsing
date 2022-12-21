import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import app_logger


logger = app_logger.get_logger(__name__)


def url_to_parse(url_site=""):
    i = 0
    while True:
    # for i in range(100):
        ua = UserAgent(verify_ssl=False)
        us_ag = ua.random
        ua = us_ag.strip()
        headers = {'Content-Type': 'text/html', 'accept': '*/*', 'user-agent': ua}
        try:
            response = requests.get(url_site, headers=headers, timeout=None)
            # print(response.encoding)
            # response.encoding = 'utf-8'
            # response.content.decode('utf-8')
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
        i += 1
    # else:
    #     print("Poproboval 10 raz otpravit")
    #     logger.error("Poproboval 10 raz otpravit, url: {url_site}".format(url_site=url_site))
    return soup, response.status_code


if __name__ == "__main__":
    pass

from util import *

userName = sys.argv[1]
password = sys.argv[2]


@retry(stop_max_attempt_number=5)
def main():
    try:
        driver = get_web_driver()
        driver.get("https://www.hmoe11.net/")
        driver.find_element_by_xpath(
            '''/html/body/div[12]/div/div[2]/div/footer/a''').click()
        driver.find_element_by_xpath(
            '''//*[@id="inn-sign__login-btn__container"]/a''').click()
        driver.find_element_by_xpath(
            '''//*[@id="inn-sign__dialog__fm"]/div/div/div/div[2]/label/span[2]/input'''
        ).send_keys(userName)
        driver.find_element_by_xpath(
            '''//*[@id="inn-sign__dialog__fm"]/div/div/div/div[3]/label/span[2]/input'''
        ).send_keys(password)
        driver.find_element_by_xpath(
            '''//*[@id="inn-sign__dialog__fm"]/footer/button''').click()
        driver.find_element_by_xpath(
            '''//*[@id="inn-nav__point-sign-daily"]''').click()
    except:
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    main()

from util import *

userName = sys.argv[1]
password = sys.argv[2]

@retry(stop_max_attempt_number=5)
def main():
    try:
        driver = get_web_driver()
        driver.get("https://cangku.icu/login")
        driver.find_element_by_xpath(
            '''//*[@id="login"]/div/form/div[3]/input''').send_keys(userName)
        driver.find_element_by_xpath(
            '''//*[@id="login"]/div/form/div[4]/input''').send_keys(password)
        driver.find_element_by_xpath(
            '''//*[@id="login"]/div/form/button''').click()
        driver.find_element_by_xpath(
            '''//*[@id="sidebar"]/div[1]/div/div[4]/ul/li[2]/a''').click()
    except:
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    main()


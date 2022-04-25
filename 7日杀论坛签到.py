from util import *

userName = sys.argv[1]
password = sys.argv[2]

@retry(stop_max_attempt_number=5)
def main():
    try:
        driver = get_web_driver()
        driver.get("https://www.7risha.com/")
        driver.find_element_by_xpath(
            '''//*[@id="jinsom-sidebar-username"]''').send_keys(userName)
        driver.find_element_by_xpath(
            '''//*[@id="jinsom-sidebar-password"]''').send_keys(password)
        driver.find_element_by_xpath(
            "/html/body/div[3]/div[1]/div/div[1]/div/div[1]").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[1]/div/div[5]").click()
    except:
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
    

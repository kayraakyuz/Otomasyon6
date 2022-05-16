from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Lcwakiki():
    url = "https://www.lcwaikiki.com/tr-TR/TR"
    CATEGORY_PAGE = (By.CSS_SELECTOR, ".buton_Image.buton_B1")  # 5
    CATEGORY_PAGE_TYPE = (By.CSS_SELECTOR, ".visible-md")  # 3
    PRODUCT_CART_TITLE = (By.CSS_SELECTOR, ".product-card__title")  # 0
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".product-card--one-of-4")  # 0
    CHOOSE_SIZE = (By.CSS_SELECTOR, "a[data-container='body")  # 0
    ADD_TO_CART = (By.CSS_SELECTOR, ".add-to-cart.button-link.add-to-cart-button")  # 0
    BASKET_PAGE_NAME = (By.CSS_SELECTOR, "svg[id='shopping-cart']")  # 4
    BASKET_PAGE = (By.CSS_SELECTOR, "a[href='https://www.lcwaikiki.com/tr-TR/TR/sepetim']")
    MAIN_PAGE_NAME = (By.CSS_SELECTOR, "a[class='main-header-logo]")
    MAIN_PAGE = (By.CSS_SELECTOR, ".main-header-logo")

    def __init__(self):
        self.driver = webdriver.Chrome("/Users/kayraakyuz/PycharmProjects/Otomasyon6/chromedriver")
        self.driver.maximize_window()
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 15)

    def test_navigate(self):
        assert self.url == self.driver.current_url, "URL HATASI"
        self.driver.execute_script("window.scrollTo(0, 1900)")
        category_page = self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[0].text
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[0].click()
        assert category_page == "Çocuk-Bebek", "KATEGORİ HATASI"

        product_cart_title = self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_CART_TITLE))[5].text
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[5].click()
        print(product_cart_title)
        assert product_cart_title == "Bisiklet Yaka Baskılı Fırfır Detaylı Kız Çocuk Tüllü Elbise", "SEÇİLEN ÜRÜN HATASI"

        choose_size = self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE))[0].text
        self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE))[0].click()
        assert choose_size == "4-5 Yaş", "BEDEN SEÇİMİ HATASI"

        self.driver.execute_script("window.scrollTo(0, 400)")

        add_to_cart = self.wait.until(ec.presence_of_all_elements_located(self.ADD_TO_CART))[0].text
        self.wait.until(ec.presence_of_all_elements_located(self.ADD_TO_CART))[0].click()
        assert add_to_cart == "SEPETE EKLE", "SEPETE EKLEME HATASI"


        basket_page = self.wait.until(ec.presence_of_all_elements_located(self.BASKET_PAGE_NAME))[0].text
        self.wait.until(ec.element_to_be_clickable(self.BASKET_PAGE)).click()
        assert basket_page == "SEPETİM", "SEPETE GİTME HATASI"

        self.wait.until(ec.element_to_be_clickable(self.MAIN_PAGE)).click()
        assert self.url == self.driver.current_url, "ANASAYFA HATASI"

    def tear_down(self):
        self.driver.quit()


def main():
    lcwakiki = Lcwakiki()
    lcwakiki.test_navigate()
    lcwakiki.tear_down()


if __name__ == '__main__':
    main()
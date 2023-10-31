from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BuyGoods(BasePage):

    URL = 'https://ua.iherb.com'
    
    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(BuyGoods.URL)

    def buy_goods(self, goods_name):

        # Знаходимо елементи класу для відкриття поля пошуку
        branded_header = self.driver.find_element(By.CLASS_NAME, "branded-header-container.header-container")
        iherb_header_search = self.driver.find_element(By.CLASS_NAME, "iherb-header-search")

        # Отримуємо поточні класи елементів поля пошуку
        branded_header_classes = branded_header.get_attribute("class")
        iherb_header_search_classes = iherb_header_search.get_attribute("class")

        # Змінюємо класи поля пошуку
        branded_header_classes += " search-open"
        iherb_header_search_classes += " active"

        # Оновлюємо класи елементів поля пошуку за допомогою JavaScript коду
        self.driver.execute_script("arguments[0].setAttribute('class', arguments[1]);", branded_header, branded_header_classes)
        self.driver.execute_script("arguments[0].setAttribute('class', arguments[1]);", iherb_header_search, iherb_header_search_classes)
       
        # Знаходимо поле пошуку товару
        search_elem = self.driver.find_element(By.ID, "txtSearch")

        # Вводимо назву товару
        search_elem.send_keys(goods_name)

        # Знаходимо кнопку пошуку
        search_btn = self.driver.find_element(By.ID, "searchBtn")
    
        # Емулюємо клік лівою кнопкою мишки
        search_btn.click()

        # Знаходимо товар
        goods_elem = self.driver.find_element(By.ID, "pid_22335")

        # Обираємо товар
        goods_elem.click()
        
        # Знаходимо кнопку "Додати в кошик"
        add_cart_goods = self.driver.find_element(By.NAME, "AddToCart")

        # Емулюємо клік лівою кнопкою мишки, та додаємо затримку для анімації
        add_cart_goods.click()
        time.sleep(2)

        # Знаходимо корзину
        carts = self.driver.find_element(By.CLASS_NAME, "checkout-button")

        # Емулюємо клік лівою кнопкою мишки
        carts.click()

        # Знаходимо поле зміни кількості товару
        count_elem = self.driver.find_element(By.ID, "react-select-2-input")

        # Вводимо кількість 5
        count_elem.send_keys(5)

        # Знаходимо елемент зміни доставки 
        delivery_elem = self.driver.find_element(By.CLASS_NAME, "css-g94so0")

        # Емулюємо клік лівою кнопкою мишки
        delivery_elem.click()
        
        # Знаходимо поле зміни країни
        country_elem = self.driver.find_element(By.CLASS_NAME, "css-y8v00p")

        # Перевіряємо значення, та вводимо "UA - Україна" за необхідності
        if country_elem != "UA - Україна":
            country_elem.send_keys("UA - Україна")
            country_elem.send_keys(Keys.ENTER)
        else:
            pass

        # Знаходимо поле зміни індексу 
        zip_elem = self.driver.find_element(By.NAME, "postal-code")

        # Вводимо значення "79496"
        zip_elem.send_keys("79496")
        zip_elem.send_keys(Keys.ENTER)

        # Знаходимо кнопку "Зберегти"
        save_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[data-qa-element="btn-save-destination"]')

        # Зберігаємо
        save_btn.click()
        time.sleep(1)

        # Знаходимо доставку Meest
        delivery_meest_elem = self.driver.find_element(By.CLASS_NAME, 'css-3ge7j2')

        # Обираємо доставку Meest
        delivery_meest_elem.click()

        # Знаходимо елемент "Оформити замовлення"
        order_elem = self.driver.find_element(By.CLASS_NAME, "css-1ijv08")

        # Створюємо замовлення
        order_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

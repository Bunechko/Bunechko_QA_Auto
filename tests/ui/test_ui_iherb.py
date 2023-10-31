from modules.ui.page_object.buy_product_iherb import BuyGoods
import pytest


@pytest.mark.iherb
def test_iherb():
    # Створення об'єкту сторінки
    add_cart = BuyGoods()

    # Відкриваємо сторінку https://ua.iherb.com
    add_cart.go_to()

    # Знаходимо товар, додаємо в корзину, переходимо до замовлення
    add_cart.buy_goods("now foods vitamin d3 5000 iu - 240 softgels")

    # Перевіряємо, що ми на сторінці введення даних в особистий кабінет
    assert add_cart.check_title("Login Pages")

    # Закриваємо браузер
    add_cart.close()

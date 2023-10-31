from modules.ui.page_object.tracking_meest import Search
import pytest


@pytest.mark.meest
def test_tracking_meest():
    # Створення об'єкту сторінки
    tracking_meest = Search()

    # Відкриваємо сторінку https://ua.meest.com
    tracking_meest.go_to()

    # Виконуємо трекінг відправлення
    tracking_meest.tracking("MYCV059863575PL")

    # Перевіряємо, що назва сторінкитака, яку ми очікуємо
    assert tracking_meest.check_title("Відстежити посилку ᐈ Meest Трекінг 【Україна】- Поштові & Транспортні послуги")

    # Закриваємо браузер
    tracking_meest.close()

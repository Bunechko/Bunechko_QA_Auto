import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    create = db.select_product_qnt_by_id(4)

    assert create[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check the number of orders equal to 1
    assert len(orders) == 1

    # Check the data structure
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"

# -------------------------------------------------------------------------------
# Project task 5. Module 28. SQL

@pytest.mark.database
def test_product_qnt_insert_text_value():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 'text')


@pytest.mark.database
def test_orders_date_update_text_value():
    db = Database()
    db.update_orders_date_by_id(1, '2 червня 2023 року')
    orders = db.get_detailed_orders()
    
    assert orders[0][4] != '2 червня 2023 року'


@pytest.mark.database
def test_product_id_insert_text_value():
    db = Database()
    db.insert_product('five', 'тестові', 'дані', 99)


@pytest.mark.database
def test_orders_date_update():
    db = Database()
    db.update_orders_date_by_id(1, "2023-06-02")
    orders = db.get_detailed_orders()

    assert orders[0][4] == "2023-06-02"


@pytest.mark.database
def test_customer_id_insert_text_value():
    db = Database()
    db.insert_customer('three', 'Юра', 'Тестер', 'Львів', '79000', 'Україна')


@pytest.mark.database
def test_customer_insert():
    db = Database()
    db.insert_customer(3, 'Юра', 'Тестер', 'Львів', '79000', 'Україна')

    customer = db.get_user_by_id(3)

    assert customer[2][0] == 3
    assert customer[2][1] == 'Юра'
    assert customer[2][2] == 'Тестер'
    assert customer[2][3] == 'Львів'
    assert customer[2][4] == '79000'
    assert customer[2][5] == 'Україна'


@pytest.mark.database
def test_order_insert():
    db = Database()
    db.insert_order(2, 3, 4, "2023-10-25")

    order = db.get_order_by_id(2)

    assert order[1][0] == 2
    assert order[1][1] == 3
    assert order[1][2] == 4
    assert order[1][3] == "2023-10-25"

# -------------------------------------------------------------------------------

from conftest import *


def test_show_my_pets(go_to_my_pets):
    """Проверка что мы находимся на странице Мои питомцы"""

    # Нажимаем на ссылку "Мои питомцы"
    pytest.driver.find_element_by_link_text("Мои питомцы").click()

    # Проверка, что мы находимся на странице "Мои питомцы"
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

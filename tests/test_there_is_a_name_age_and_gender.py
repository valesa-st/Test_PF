from conftest import *


def test_there_is_a_name_age_and_gender(go_to_my_pets):
    """Поверка, что на странице со списком моих питомцев, у всех питомцев есть имя, возраст, фото и порода"""

    # Сохраняем в переменную pet_data элементы с данными о питомцах
    pet_data = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    # Перебираем данные из pet_data, оставляем имя, возраст и породу, остальное изменяем на пустую строку
    # и разделяем пробелом.Находим количество элементов в получившемся списке и сравниваем их
    # с ожидаемым результатом
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        result = len(split_data_pet)
        assert result == 3
        assert pet_data[i].get_attribute('src') != ''

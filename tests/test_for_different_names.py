from conftest import *


def test_all_pets_have_different_names(go_to_my_pets):
    """Поверяем что у всех питомцев на странице с моими питомцами разные имена """

    # В переменную pet_data сохраняем элементы с данными о питомцах
    pet_data = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    # Перебираем данные из pet_data, оставляем имя, возраст и породу, остальное меняем на пустую строку
    # И разделяем по пробелу. Выбираем имена и добавляем их в список pets_name.
    pets_name = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])

    # Перебираем имена, если имя повторяется, то прибавляем единицу к счетчику r.
    # Проверяем, если r == 0, то повторяющихся имен нет.
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
    assert r == 0
    print(f'\n {r}')
    print(f'\n {pets_name}')

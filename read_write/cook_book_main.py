import os

# Задача №1
# Создаем класс Рецепт
class Recipe:
    def __init__(self, name, ingredients):
        """
        Класс для представления рецепта.
        Аргументы:
        name (str): Название рецепта.
        ingredients (list): Список ингредиентов в формате 
        [название, количество, единицы измерения].
        """
        self.name = name
        self.ingredients = ingredients

# Создаем список рецептов и словарь рецептов
recipes = []
cook_book = {}

# Проверяем и создаем директорию для файлов, если она не существует
directory = 'read_write/files'
if not os.path.exists(directory):
    os.makedirs(directory)

with open(f"{directory}/recipes.txt", 'r', encoding='utf-8') as file:
    recipe_data = file.read().split('\n\n')

for recipe_str in recipe_data:
    recipe_info = recipe_str.split('\n')
    name = recipe_info[0]
    ingredients = [ingredient.split('|') for ingredient in recipe_info[1:]]
    recipes.append(Recipe(name, ingredients))

    cook_book[name] = []
    for ing in ingredients:
        if len(ing) >= 3:
            ingredient_dict = {
                'ingredient_name': ing[0].strip(),
                'quantity': ing[1].strip() if len(ing) > 1 else "",
                'measure': ing[2].strip() if len(ing) > 2 else ""
            }
            cook_book[name].append(ingredient_dict)

with open(f"{directory}/cookbook.txt", "w", encoding='utf-8') as file:
    for recipe in recipes:
        file.write(f"{recipe.name}\n")
        file.write(f"{len(recipe.ingredients)}\n")
        for ingredient in recipe.ingredients:
            file.write(" | ".join([str(comp).strip() for comp in ingredient]) + "\n")

# Вывод словаря рецептов
print("\nСловарь рецептов, : ")
print(cook_book)
print()

# Вывод словаря рецептов в формате JSON
print("Список блюд кулинарной книги: ")
print(", ".join(cook_book.keys()))
print()

# Вывод словаря рецептов, как в txt
print("\n Содержание рецептуры блюд: ")

# Просмотр списка рецептов
for recipe in recipes:
    print(f"Название блюда: {recipe.name}")
    print("Ингредиенты:")
    for ingredient in recipe.ingredients:
        print(" | ".join([comp.strip() for comp in ingredient]))
    print("\n")

# Задача № 2
# Функции для работы с рецептами и ингредиентами

def get_shop_list_by_dishes(dishes, person_count):
    """
     Функция для создания списка ингредиентов для закупки на основе списка 
     блюд и количества персон.
     Аргументы:
     dishes (list): Список блюд, для которых необходимо подготовить 
     список ингредиентов.
     person_count (int): Количество персон, для которых нужно рассчитать 
     количество ингредиентов.
     Возвращает:
     shop_list (dict): Словарь с ингредиентами для закупки, 
     где ключ - название ингредиента,
     значение - словарь с количеством и единицей измерения.
     Пример использования:
     result = get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос'], 2)
     """
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient.get('ingredient_name')
                quantity = int(ingredient.get('quantity', 0)) * person_count
                measure = ingredient.get('measure', '')
                if name:
                    if name not in shop_list:
                        shop_list[name] = {
                            'quantity': quantity, 'measure': measure}
                    else:
                        shop_list[name]['quantity'] += quantity
                else:
                    print(f"Ингредиент не найден для блюда '{dish}'.")
        else:
            print(f"Блюдо '{dish}' не найдено в кулинарной книге.")
    return shop_list

# Вызов функции создания словаря для шопинга, формат dict{}
result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 10)
print('Создан словарь shop_list:\n', result)
print()
def write_shop_list_to_file(shop_list, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("СПИСОК ИНГРЕДИЕНТОВ для закупки:\n")
        file.write("---------------------------------\n")
        for ingredient, data in shop_list.items():
            file.write(
                f"{ingredient} - {data['quantity']} {data['measure']}\n")

# Вызова функции для записи списка ингредиентов в файл
write_shop_list_to_file(result, 'read_write/files/shop_list.txt')
def print_shop_list(shop_list):
    """
       Функция для печати списка ингредиентов для закупки на экран.
       Аргументы:
       shop_list (dict): Словарь с ингредиентами для закупки.
       """
    print("СПИСОК ИНГРЕДИЕНТОВ\n для закупки на 10 персон\n меню:\
         запеченый картофель и омлет:")
    print("---------------------------------")
    for ingredient, data in shop_list.items():
        print(f"\t{ingredient} - {data['quantity']} {data['measure']}")
print()

# Вызова функции для печати списка ингредиентов
print_shop_list(result)
print()

# Блока для работы с файлом
def print_cooking():
    with open(f'{directory}/cooking.txt', 'r', encoding='utf-8') as file:
        print(file.read())

def add_recipe(name, ingredients):
    """
    Функция для добавления нового рецепта в словарь cook_book и файл.
    Аргументы:
    name (str): Название рецепта.
    ingredients (list): Список ингредиентов в формате 
    [название, количество, единицы измерения].
    """
    # Проверка наличия имени рецепта и ингредиентов
    if not name or not ingredients:
        print(f"Добавление рецепта: {name}") # Отладочное сообщение
        return

    new_recipe = Recipe(name, ingredients)
    recipes.append(new_recipe)

    cook_book[name] = []
    for ing in ingredients:
        # Создаем словарь для хранения информации об ингредиенте
        ingredient_dict = {}
        # Добавляем обязательные компоненты
        ingredient_dict['ingredient_name'] = ing[0].strip()
        # Добавляем дополнительные компоненты, если они есть
        if len(ing) > 1:
            ingredient_dict['quantity'] = ing[1].strip()
        if len(ing) > 2:
            ingredient_dict['measure'] = ing[2].strip()
        # Добавляем в список ингредиентов для рецепта
        cook_book[name].append(ingredient_dict)

    # Записываем рецепт в файл
    with open(f'{directory}/cooking.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name}\n')
        file.write(f'{len(ingredients)}\n') # Записываем количество ингредиентов
        for ing in ingredients:
            # Формируем строку для записи в ожидаемом формате
            ing_str = ' | '.join(ing)
            file.write(f'{ing_str}\n')
        file.write('\n')


add_recipe('Салат Цезарь', [
    ['Куриное филе', '200', 'г'],
    ['Салат Романо', '1', 'шт'],
    ['Соус Цезарь', '2', 'ст.л']
])

# Отладочное сообщение
print(f"Рецепт '{name}' успешно добавлен.") 


def delete_recipe(name):
    """
    Функция для удаления рецепта по названию.
    Аргументы:
    name (str): Название рецепта, который нужно удалить.
    Например: delete_recipe('Омлет')
    """
    for recipe in recipes:
        if recipe.name == name:
            recipes.remove(recipe)
            del cook_book[name]
            break

def user_interaction():
    """Функция для общения с пользователем."""
    print("Добро пожаловать! Что бы вы хотели сделать?")
    print("1. Добавить новый рецепт (название с заглавной буквы).")
    print("2. Удалить рецепт (название с заглавной буквы).")
    print("3. Получить список ингредиентов для закупки.")
    print("4. Выйти.")

    choice = input("Выберите действие (1/2/3/4): ")

    if choice == '1':
        name = input("Введите название нового рецепта: ")
        ingredients = []
        num_ingredients = int(input("Введите количество ингредиентов: "))
        for _ in range(num_ingredients):
            ingredient_name = input("Введите название ингредиента: ")
            quantity = input("Введите количество ингредиента: ")
            measure = input("Введите единицы измерения: ")
            ingredients.append([ingredient_name, quantity, measure])
        add_recipe(name, ingredients)
        print("Новый рецепт добавлен!")
    elif choice == '2':
        name = input("Введите название рецепта, который нужно удалить: ")
        delete_recipe(name)
        print("Рецепт удален!")
    elif choice == '3':
        dishes = input("Введите названия блюд через запятую (название с заглавной буквы): ").split(',')
        person_count = int(input("Введите количество персон: "))
        result = get_shop_list_by_dishes(dishes, person_count)
        if result:
            write_shop_list_to_file(result, 'shop_list.txt')
            print_shop_list(result)
        else:
            print("Не удалось сформировать список ингредиентов для закупки.")
    elif choice == '4':
        print("До свидания! Спасибо за использование нашего сервиса.")
    else:
        print("Некорректный ввод. Пожалуйста, \
            Пожалуйста, выберите действие из предложенных.")

# Вызов функции для выполнения блока общения с пользователем
user_interaction()

__name__ == '__main__'
user_interaction()
# Блок для работы с файлом            
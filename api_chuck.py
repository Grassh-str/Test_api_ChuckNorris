import requests

class Test_new_joke():

    """Создание новой шутки"""

    def __init__(self):
        pass

    def get_categories(self):

        """Получение категориb шуток"""

        url_categories = "https://api.chucknorris.io/jokes/categories"
        print("Получение категорий шуток по ссылке - " + url_categories)
        all_categories_get = requests.get(url_categories)
        assert all_categories_get.status_code == 200
        if all_categories_get.status_code == 200:
            print("Статус код: 200\nКатегории получены\n")
        all_categories = all_categories_get.json()

        global categories_ok
        categories_ok = False

        for f in all_categories:                        # Проверка введеной категории и получение шутки

                    if f == user_categories:
                        url = "https://api.chucknorris.io/jokes/random?category=" + f
                        print("Получение шутки по ссылке -" + url)
                        result = requests.get(url)
                        assert result.status_code == 200
                        print("Статус код: 200\nШутка в данной категории получена:")
                        joke_get = result.json()
                        joke = joke_get.get('value')
                        print(joke + "\n")
                        categories_ok = True

    def description(self):

        """Получение списка категорий"""

        url_categories = "https://api.chucknorris.io/jokes/categories"
        all_categories_get = requests.get(url_categories)
        assert all_categories_get.status_code == 200
        all_categories = all_categories_get.json()
        for f in all_categories:
            print(f)


user_categories = input("Введите название категории из которой хотите получить шутку: ")
cat = Test_new_joke()
cat.get_categories()

while not categories_ok:
    print("Такой категории не существует.\nСписок категорий:")
    cat.description()
    user_categories = input("Введите название категории из этого списка: ")
    cat.get_categories()
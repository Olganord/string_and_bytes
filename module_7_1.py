with open('products.txt', 'a') as an_alias_for_it:
    pass


class Product:

    def __init__(self, name, weight, category):
        self.name = name  # Название продукта
        self.weight = weight  # Общий вес товара
        self.category = category  # Категория товара

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"  # Формат для вывода


class Shop:
    # open('product.txt', 'r')

    def __init__(self):
        self._filename = 'products.txt'  # Имя файла для хранения продуктов

    def get_products(self):
        with open(self._filename, 'r') as f:  # Открываем файл для чтения
            return f.read().strip()  # Читаем и возвращаем содержимое. read считывает, strip
            # удаляет символы или пробелы из начала и конца исходной строки.

    def add(self, *products):
        existing_products = self.get_products().splitlines()  # Получаем существующие продукты
        with open(self._filename, 'a') as f:  # Открываем файл для добавления
            for product in products:
                if product.name in (p.split(',')[0] for p in existing_products):  # Проверка на дубли
                    print(f"Продукт {product} уже есть в магазине")
                else:

                    f.write(str(product) + '\n')  # Записываем новый продукт


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


import csv
import os


class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл items1.csv поврежден"

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        elif issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return Exception  # Исключение

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):

        return f"{self.__name}"

    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, name):

        self.__name = name

        if len(self.__name) > 10:
            self.__name = name[:9]
            return f'{self.__name}'

        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_name):

        Item.all.clear()

        path = os.path.join(os.path.dirname(__file__), '..', file_name)

        if not os.path.exists(path):
            raise FileNotFoundError('Отсутствует файл item.csv')

        with open(path, 'r', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            headers = list(reader)[0]
            if headers != ['name', 'price', 'quantity']:
                raise InstantiateCSVError
            else:
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(string: str):
        return int(float(string))




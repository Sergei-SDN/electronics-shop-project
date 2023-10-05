from src.item import Item, InstantiateCSVError

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    try:
        Item.instantiate_from_csv('src/item.csv')
    except FileNotFoundError as e:
        print(e) # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    try:
        Item.instantiate_from_csv('src/items1.csv')
    except InstantiateCSVError as e:
        print(e) # InstantiateCSVError: Файл item1.csv поврежден
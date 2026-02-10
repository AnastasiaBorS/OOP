# TODO Написать 3 класса с документацией и аннотацией типов
# TODO работоспособность экземпляров класса проверить с помощью doctest
import doctest
from abc import ABC, abstractmethod

class MusicalInstrument(ABC):
    def __init__(self, name: str, weight_kg: float, price_usd: float):
        """
        Создание и подготовка к работе объекта "Музыкальный инструмент"

        :param name: Название инструмента
        :param weight_kg: Вес инструмента в килограммах
        :param price_usd: Цена инструмента в долларах США

        Примеры:
        >>> guitar = MusicalInstrument("Electric Guitar", 4.5, 1200.0)
        >>> piano = MusicalInstrument("Grand Piano", 320.0, 8500.0)
        """
        if not isinstance(name, str):
            raise TypeError("Название инструмента должно быть строкой")
        if len(name.strip()) == 0:
            raise ValueError("Название инструмента не может быть пустым")
        self.name = name.strip()

        if not isinstance(weight_kg, (int, float)):
            raise TypeError("Вес инструмента должен быть типа int или float")
        if weight_kg <= 0:
            raise ValueError("Вес инструмента должен быть положительным числом")
        self.weight_kg = float(weight_kg)

        if not isinstance(price_usd, (int, float)):
            raise TypeError("Цена инструмента должна быть типа int или float")
        if price_usd < 0:
            raise ValueError("Цена инструмента не может быть отрицательной")
        self.price_usd = float(price_usd)

    def calculate_price_per_kg(self) -> float:
        """
        Расчет стоимости одного килограмма инструмента.

        :return: Цена за один килограмм в долларах США

        Примеры:
        >>> guitar = MusicalInstrument("Electric Guitar", 4.5, 1200.0)
        >>> guitar.calculate_price_per_kg()
        """
        ...

    def apply_discount(self, discount_percent: float) -> None:
        """
        Применение скидки к цене инструмента.

        :param discount_percent: Процент скидки (от 0 до 100)
        :raise ValueError: Если процент скидки выходит за допустимые границы

        Примеры:
        >>> guitar = MusicalInstrument("Electric Guitar", 4.5, 1200.0)
        >>> guitar.apply_discount(15.0)  # 15% скидка
        """
        if not isinstance(discount_percent, (int, float)):
            raise TypeError("Процент скидки должен быть типа int или float")
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Процент скидки должен быть в диапазоне от 0 до 100")
        ...

    @abstractmethod
    def play_note(self, note: str) -> str:
        """
        Воспроизведение ноты на инструменте.

        :param note: Название ноты (например, "C4", "A#5")
        :return: Описание воспроизведенного звука
        :raise ValueError: Если нота не поддерживается инструментом

        Примеры:
        >>> guitar = MusicalInstrument("Electric Guitar", 4.5, 1200.0)
        >>> guitar.play_note("E2")
        """
        ...


class Book:
    def __init__(self, title: str, author: str, publication_year: int, pages_count: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param publication_year: Год публикации
        :param pages_count: Количество страниц

        Примеры:
        >>> book = Book("1984", "George Orwell", 1949, 328)
        >>> novel = Book("Pride and Prejudice", "Jane Austen", 1813, 432)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if len(title.strip()) == 0:
            raise ValueError("Название книги не может быть пустым")
        self.title = title.strip()

        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть строкой")
        if len(author.strip()) == 0:
            raise ValueError("Имя автора не может быть пустым")
        self.author = author.strip()

        if not isinstance(publication_year, int):
            raise TypeError("Год публикации должен быть целым числом")
        current_year = 2024  # можно импортировать datetime для точного значения
        if publication_year < 0 or publication_year > current_year:
            raise ValueError(f"Год публикации должен быть между 0 и {current_year}")
        self.publication_year = publication_year

        if not isinstance(pages_count, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages_count <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages_count = pages_count

    def calculate_reading_time(self, words_per_minute: int = 200) -> float:
        """
        Расчет примерного времени чтения книги.

        :param words_per_minute: Средняя скорость чтения (слов в минуту)
        :return: Время чтения в часах
        :raise ValueError: Если скорость чтения некорректна

        Примеры:
        >>> book = Book("1984", "George Orwell", 1949, 328)
        >>> book.calculate_reading_time(250)  # для скорости 250 слов в минуту
        """
        if not isinstance(words_per_minute, int):
            raise TypeError("Скорость чтения должна быть целым числом")
        if words_per_minute <= 0:
            raise ValueError("Скорость чтения должна быть положительным числом")
        ...

    def is_antique(self, current_year: int = 2024) -> bool:
        """
        Проверка, является ли книга антикварной (старше 100 лет).

        :param current_year: Текущий год для расчета
        :return: True если книга старше 100 лет, иначе False

        Примеры:
        >>> book = Book("1984", "George Orwell", 1949, 328)
        >>> book.is_antique(2024)
        >>> novel = Book("Pride and Prejudice", "Jane Austen", 1813, 432)
        >>> novel.is_antique(2024)
        """
        if not isinstance(current_year, int):
            raise TypeError("Текущий год должен быть целым числом")
        ...

    def get_book_age(self, current_year: int = 2024) -> int:
        """
        Получение возраста книги в годах.

        :param current_year: Текущий год для расчета
        :return: Возраст книги в годах

        Примеры:
        >>> book = Book("1984", "George Orwell", 1949, 328)
        >>> book.get_book_age(2024)
        """
        ...


class Smartphone:
    def __init__(self, brand: str, model: str, battery_capacity_mah: int, storage_gb: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд производителя
        :param model: Модель смартфона
        :param battery_capacity_mah: Емкость батареи в мАч
        :param storage_gb: Объем памяти в гигабайтах

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 15", 3349, 128)
        >>> android = Smartphone("Samsung", "Galaxy S23", 3900, 256)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if len(brand.strip()) == 0:
            raise ValueError("Бренд не может быть пустым")
        self.brand = brand.strip()

        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if len(model.strip()) == 0:
            raise ValueError("Модель не может быть пустой")
        self.model = model.strip()

        if not isinstance(battery_capacity_mah, int):
            raise TypeError("Емкость батареи должна быть целым числом")
        if battery_capacity_mah <= 0:
            raise ValueError("Емкость батареи должна быть положительным числом")
        self.battery_capacity_mah = battery_capacity_mah

        if not isinstance(storage_gb, int):
            raise TypeError("Объем памяти должен быть целым числом")
        if storage_gb <= 0:
            raise ValueError("Объем памяти должен быть положительным числом")
        self.storage_gb = storage_gb

    def estimate_battery_life(self, screen_on_hours: float, standby_hours: float) -> float:
        """
        Оценка времени работы батареи.

        :param screen_on_hours: Часы использования с включенным экраном в день
        :param standby_hours: Часы в режиме ожидания в день
        :return: Общее время работы в днях
        :raise ValueError: Если параметры использования некорректны

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 15", 3349, 128)
        >>> phone.estimate_battery_life(5.0, 19.0)  # 5 часов экрана + 19 часов ожидания в день
        """
        if not isinstance(screen_on_hours, (int, float)):
            raise TypeError("Часы использования экрана должны быть числом")
        if screen_on_hours < 0:
            raise ValueError("Часы использования экрана не могут быть отрицательными")

        if not isinstance(standby_hours, (int, float)):
            raise TypeError("Часы ожидания должны быть числом")
        if standby_hours < 0:
            raise ValueError("Часы ожидания не могут быть отрицательными")
        ...

    def can_store_apps(self, app_sizes_gb: list[float]) -> bool:
        """
        Проверка, поместятся ли приложения в память смартфона.

        :param app_sizes_gb: Список размеров приложений в гигабайтах
        :return: True если все приложения поместятся, иначе False
        :raise ValueError: Если размеры приложений некорректны

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 15", 3349, 128)
        >>> phone.can_store_apps([2.5, 1.8, 0.5, 4.2])  # размеры 4 приложений
        """
        if not isinstance(app_sizes_gb, list):
            raise TypeError("Размеры приложений должны быть представлены списком")

        for size in app_sizes_gb:
            if not isinstance(size, (int, float)):
                raise TypeError("Размер приложения должен быть числом")
            if size < 0:
                raise ValueError("Размер приложения не может быть отрицательным")
        ...

    def get_full_name(self) -> str:
        """
        Получение полного названия смартфона (бренд + модель).

        :return: Полное название смартфона

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 15", 3349, 128)
        >>> phone.get_full_name()
        """
        ...


if __name__ == "__main__":
    doctest.testmod(verbose=True)
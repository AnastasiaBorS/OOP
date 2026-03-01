class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Название книги (только для чтения)."""
        return self._name

    @property
    def author(self) -> str:
        """Автор книги (только для чтения)."""
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Бумажная книга с количеством страниц."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # используем сеттер свойства pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def __repr__(self) -> str:
        # Добавляем в repr информацию о количестве страниц
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, pages={self.pages!r})")


class AudioBook(Book):
    """Аудиокнига с продолжительностью в часах."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # используем сеттер свойства duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной")
        self._duration = float(value)

    def __repr__(self) -> str:
        # Добавляем в repr информацию о продолжительности
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, duration={self.duration!r})")
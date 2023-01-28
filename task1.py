class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, amount):
        if not isinstance(amount, int):
            raise TypeError('Number of pages should be integer.')
        if amount <= 0:
            raise ValueError('Number of pages should be positive.')
        self._pages = amount


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, amount):
        if not isinstance(amount, float):
            raise TypeError('Duration should be float-typed.')
        if amount <= 0:
            raise ValueError('Duration should be positive.')
        self._duration = amount

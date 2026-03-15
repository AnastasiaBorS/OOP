"""
Модуль демонстрирует наследование на примере банковских счетов.
Базовый класс Account представляет общий банковский счёт.
Дочерний класс SavingsAccount добавляет ограничение минимального остатка.
"""

from typing import Union

class Account:
    """
    Базовый класс банковского счёта.

    Атрибуты:
        _account_number (str): номер счёта (непубличный, защищён от прямого изменения).
        _holder (str): владелец счёта (непубличный).
        _balance (float): текущий баланс (непубличный, доступ через методы).

    Инкапсуляция применена для защиты данных счёта от некорректного изменения извне.
    """

    def __init__(self, account_number: str, holder: str, initial_balance: float = 0.0) -> None:
        """
        Инициализирует счёт.

        Аргументы:
            account_number: уникальный номер счёта.
            holder: имя владельца.
            initial_balance: начальный баланс (по умолчанию 0.0).
        """
        self._account_number = account_number
        self._holder = holder
        self._balance = initial_balance

    def deposit(self, amount: float) -> None:
        """
        Вносит средства на счёт.

        Аргументы:
            amount: сумма пополнения (должна быть положительной).

        Исключения:
            ValueError: если amount <= 0.
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Снимает средства со счёта.

        Аргументы:
            amount: сумма снятия.

        Исключения:
            ValueError: если amount <= 0 или недостаточно средств.
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount

    def get_balance(self) -> float:
        """Возвращает текущий баланс."""
        return self._balance

    def __str__(self) -> str:
        """Пользовательское строковое представление счёта."""
        return f"Счёт {self._account_number}, владелец: {self._holder}, баланс: {self._balance:.2f}"

    def __repr__(self) -> str:
        """Официальное строковое представление для разработчиков."""
        return f"Account('{self._account_number}', '{self._holder}', {self._balance})"


class SavingsAccount(Account):
    """
    Сберегательный счёт, наследующий Account.

    Добавляет требование поддержания минимального остатка.

    Атрибуты:
        _min_balance (float): минимально допустимый остаток на счёте (непубличный).
    """

    def __init__(self, account_number: str, holder: str, initial_balance: float = 0.0,
                 min_balance: float = 100.0) -> None:
        """
        Расширяет конструктор базового класса, добавляя минимальный остаток.

        Аргументы:
            account_number: номер счёта.
            holder: владелец.
            initial_balance: начальный баланс.
            min_balance: минимальный остаток (по умолчанию 100.0).
        """
        super().__init__(account_number, holder, initial_balance)
        self._min_balance = min_balance

    def withdraw(self, amount: float) -> None:
        """
        Перегружает метод снятия средств.

        Причина перегрузки: для сберегательного счёта действует требование поддержания
        минимального остатка. Данный метод проверяет, что после снятия баланс не станет
        ниже _min_balance.

        Аргументы:
            amount: сумма снятия.

        Исключения:
            ValueError: если amount <= 0, недостаточно средств или нарушается
                        условие минимального остатка.
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if self._balance - amount < self._min_balance:
            raise ValueError(f"Снятие невозможно: остаток не может быть ниже {self._min_balance}")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount

    def apply_interest(self, rate: float) -> None:
        """
        Начисляет проценты на остаток (новый метод, специфичный для сберегательного счёта).

        Аргументы:
            rate: годовая процентная ставка (например, 0.05 для 5%).
        """
        if rate < 0:
            raise ValueError("Процентная ставка не может быть отрицательной")
        self._balance += self._balance * rate

    def __str__(self) -> str:
        """
        Перегружает строковое представление для отображения типа счёта.
        """
        return (f"Сберегательный счёт {self._account_number}, владелец: {self._holder}, "
                f"баланс: {self._balance:.2f}, мин. остаток: {self._min_balance}")

    def __repr__(self) -> str:
        """
        Перегружает официальное представление с учётом дочернего класса.
        """
        return (f"SavingsAccount('{self._account_number}', '{self._holder}', "
                f"{self._balance}, min_balance={self._min_balance})")


# Пример использования (для демонстрации, в итоговом ответе может отсутствовать)
if __name__ == "__main__":
    acc = Account("12345", "Иван Петров", 500)
    print(acc)
    acc.deposit(200)
    print(acc)
    acc.withdraw(100)
    print(acc)

    sav = SavingsAccount("67890", "Мария Сидорова", 1000, min_balance=200)
    print(sav)
    sav.withdraw(700)  # OK: останется 300 >= 200
    print(sav)
    # sav.withdraw(150)  # Ошибка: остаток станет 150 < 200
    sav.apply_interest(0.03)
    print(sav)
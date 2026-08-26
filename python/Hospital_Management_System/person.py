"""Base module containing the abstract Person class.

Every human entity in the Hospital Management System (Patient, Staff,
Doctor, Nurse ...) inherits from this class so that shared attributes
(national ID, name, age, phone) and behaviour (view_info) live in one
place only.

All attributes are kept **private** (name-mangled with a double leading
underscore) and exposed to the outside world only through ``@property``
getters/setters, so callers cannot bypass validation by writing to the
attribute directly.
"""

from abc import ABC, abstractmethod


class Person(ABC):
    """Abstract base class representing any person known to the hospital.

    This class cannot be instantiated directly (it is abstract). Concrete
    subclasses such as ``Patient`` or ``Staff`` must call
    ``super().__init__(...)`` inside their own constructor.

    Private attributes:
        __national_id (str): The person's national identification number.
        __name (str): The person's full name.
        __age (int): The person's age in years.
        __phone (int): The person's contact phone number.
    """

    @abstractmethod
    def __init__(self, national_id: str, name: str, age: int, phone: int) -> None:
        """Initialize the common attributes shared by every person.

        Args:
            national_id: The person's national identification number.
            name: The person's full name.
            age: The person's age in years.
            phone: The person's contact phone number.
        """
        self.__national_id: str = ""
        self.__name: str = ""
        self.__age: int = 0
        self.__phone: int = 0

        self.national_id = national_id
        self.name = name
        self.age = age
        self.phone = phone

    # ------------------------------------------------------------------ #
    # national_id
    # ------------------------------------------------------------------ #
    @property
    def national_id(self) -> str:
        """str: The person's national identification number."""
        return self.__national_id

    @national_id.setter
    def national_id(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("national_id cannot be empty.")
        self.__national_id = str(value).strip()

    # ------------------------------------------------------------------ #
    # name
    # ------------------------------------------------------------------ #
    @property
    def name(self) -> str:
        """str: The person's full name."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("name cannot be empty.")
        self.__name = str(value).strip()

    # ------------------------------------------------------------------ #
    # age
    # ------------------------------------------------------------------ #
    @property
    def age(self) -> int:
        """int: The person's age in years."""
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        value = int(value)
        if value < 0 or value > 150:
            raise ValueError("age must be a realistic value between 0 and 150.")
        self.__age = value

    # ------------------------------------------------------------------ #
    # phone
    # ------------------------------------------------------------------ #
    @property
    def phone(self) -> int:
        """int: The person's contact phone number."""
        return self.__phone

    @phone.setter
    def phone(self, value: int) -> None:
        value = int(value)
        if value < 0:
            raise ValueError("phone must be a positive number.")
        self.__phone = value

    def view_info(self) -> str:
        """Return a human readable summary of the person's basic data.

        Returns:
            A formatted string containing the national ID, name, age and
            phone number.
        """
        return (
            f"National ID: {self.national_id} | Name: {self.name} | "
            f"Age: {self.age} | Phone: {self.phone}"
        )

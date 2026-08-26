"""Module containing the Staff class.

Staff is any employed person at the hospital (doctors, nurses,
receptionists, ...). It extends ``Person`` with employment related data,
kept private and exposed through properties.
"""

from person import Person


class Staff(Person):
    """Represents a hospital employee.

    Private attributes:
        __employee_id (str): Unique identifier assigned to the employee.
        __joining_date (str): The date the employee joined the hospital.
    """

    def __init__(
        self,
        national_id: str,
        name: str,
        age: int,
        phone: int,
        employee_id: str,
        joining_date: str,
    ) -> None:
        """Initialize a staff member.

        Args:
            national_id: The employee's national identification number.
            name: The employee's full name.
            age: The employee's age in years.
            phone: The employee's contact phone number.
            employee_id: Unique identifier assigned to the employee.
            joining_date: The date the employee joined the hospital.
        """
        super().__init__(national_id, name, age, phone)
        self.__employee_id: str = ""
        self.__joining_date: str = ""

        self.employee_id = employee_id
        self.joining_date = joining_date

    @property
    def employee_id(self) -> str:
        """str: Unique identifier assigned to the employee."""
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("employee_id cannot be empty.")
        self.__employee_id = str(value).strip()

    @property
    def joining_date(self) -> str:
        """str: The date the employee joined the hospital."""
        return self.__joining_date

    @joining_date.setter
    def joining_date(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("joining_date cannot be empty.")
        self.__joining_date = str(value).strip()

    def view_info(self) -> str:
        """Return the staff member's personal and employment information.

        Returns:
            A formatted string combining the base person info with the
            employee ID and joining date.
        """
        base = super().view_info()
        return f"{base} | Employee ID: {self.employee_id} | Joining Date: {self.joining_date}"

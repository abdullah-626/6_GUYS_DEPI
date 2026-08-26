"""Module containing the Nurse class."""

from typing import Union

from staff import Staff
from patient import Patient


class Nurse(Staff):
    """Represents a nurse working at the hospital.

    Private attributes:
        __shift (str): The nurse's working shift (e.g. "Morning", "Night").
        __certifications (str): Any professional certifications the nurse holds.
    """

    def __init__(
        self,
        national_id: str,
        name: str,
        age: int,
        phone: int,
        employee_id: str,
        joining_date: str,
        shift: str,
        certifications: str = "",
    ) -> None:
        """Initialize a nurse.

        Args:
            national_id: The nurse's national identification number.
            name: The nurse's full name.
            age: The nurse's age in years.
            phone: The nurse's contact phone number.
            employee_id: Unique identifier assigned to the nurse.
            joining_date: The date the nurse joined the hospital.
            shift: The nurse's working shift.
            certifications: Any professional certifications the nurse holds.
        """
        super().__init__(national_id, name, age, phone, employee_id, joining_date)

        self.__shift: str = ""
        self.__certifications: str = ""

        self.shift = shift
        self.certifications = certifications

    @property
    def shift(self) -> str:
        """str: The nurse's working shift."""
        return self.__shift

    @shift.setter
    def shift(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("shift cannot be empty.")
        self.__shift = str(value).strip()

    @property
    def certifications(self) -> str:
        """str: Any professional certifications the nurse holds."""
        return self.__certifications

    @certifications.setter
    def certifications(self, value: str) -> None:
        self.__certifications = str(value).strip()

    def take_vitals(self, patient: Union[Patient, str]) -> None:
        """Print a message indicating vitals are being taken for the patient.

        Args:
            patient: The ``Patient`` object (or a plain name) being checked.
        """
        patient_name = patient.name if hasattr(patient, "name") else patient
        print(f"Nurse {self.name} is taking vitals for patient: {patient_name}")

    def view_info(self) -> str:
        """Return the nurse's full information including shift details.

        Returns:
            A formatted string combining staff info with shift and
            certifications.
        """
        base_info = super().view_info()
        return f"{base_info} | Shift: {self.shift} | Certifications: {self.certifications}"

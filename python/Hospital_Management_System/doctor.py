"""Module containing the Doctor class."""

from typing import Union

from staff import Staff
from patient import Patient


class Doctor(Staff):
    """Represents a doctor working at the hospital.

    Private attributes:
        __specialty (str): The doctor's medical specialty (e.g. "Cardiology").
        __consultation_fee (float): The fee charged for a consultation.
        __license_number (str): The doctor's medical license number.
    """

    def __init__(
        self,
        national_id: str,
        name: str,
        age: int,
        phone: int,
        employee_id: str,
        joining_date: str,
        specialty: str,
        consultation_fee: float,
        license_number: str = "",
    ) -> None:
        """Initialize a doctor.

        Args:
            national_id: The doctor's national identification number.
            name: The doctor's full name.
            age: The doctor's age in years.
            phone: The doctor's contact phone number.
            employee_id: Unique identifier assigned to the doctor.
            joining_date: The date the doctor joined the hospital.
            specialty: The doctor's medical specialty.
            consultation_fee: The fee charged for a consultation.
            license_number: The doctor's medical license number.
        """
        super().__init__(national_id, name, age, phone, employee_id, joining_date)

        self.__specialty: str = ""
        self.__consultation_fee: float = 0.0
        self.__license_number: str = ""

        self.specialty = specialty
        self.consultation_fee = consultation_fee
        self.license_number = license_number

    @property
    def specialty(self) -> str:
        """str: The doctor's medical specialty."""
        return self.__specialty

    @specialty.setter
    def specialty(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("specialty cannot be empty.")
        self.__specialty = str(value).strip()

    @property
    def consultation_fee(self) -> float:
        """float: The fee charged for a consultation."""
        return self.__consultation_fee

    @consultation_fee.setter
    def consultation_fee(self, value: float) -> None:
        value = float(value)
        if value < 0:
            raise ValueError("consultation_fee cannot be negative.")
        self.__consultation_fee = value

    @property
    def license_number(self) -> str:
        """str: The doctor's medical license number."""
        return self.__license_number

    @license_number.setter
    def license_number(self, value: str) -> None:
        self.__license_number = str(value).strip()

    def prescribe_medicine(self, patient: Union[Patient, str], medicine_details: str) -> None:
        """Print a prescription message for the given patient.

        Args:
            patient: The ``Patient`` object (or a plain name) to prescribe for.
            medicine_details: A description of the prescribed medicine/dosage.
        """
        patient_name = patient.name if hasattr(patient, "name") else patient
        print(f"Doctor {self.name} prescribed: {medicine_details} for Patient {patient_name}")

    def examine_patient(self, patient: Union[Patient, str]) -> None:
        """Print a message indicating the doctor is examining the patient.

        Args:
            patient: The ``Patient`` object (or a plain name) being examined.
        """
        patient_name = patient.name if hasattr(patient, "name") else patient
        print(f"Doctor {self.name} is examining patient: {patient_name}")

    def view_info(self) -> str:
        """Return the doctor's full information including medical details.

        Returns:
            A formatted string combining staff info with specialty, fee
            and license number.
        """
        base_info = super().view_info()
        return (
            f"{base_info} | Specialty: {self.specialty} | "
            f"Fee: {self.consultation_fee} | License: {self.license_number}"
        )

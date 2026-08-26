"""Module containing the Patient class."""

from __future__ import annotations

from typing import List, TYPE_CHECKING

from person import Person

if TYPE_CHECKING:
    from appointment import Appointment
    from medical_record import MedicalRecord


class Patient(Person):
    """Represents a patient registered at the hospital.

    Private attributes:
        __blood_group (str): The patient's blood group (e.g. "O+").
        __admission_date (str): The date the patient was admitted.
        __medical_records (List[MedicalRecord]): History of medical records.
        __appointments (List[Appointment]): Appointments requested by the patient.
    """

    def __init__(
        self,
        national_id: str,
        name: str,
        age: int,
        phone: int,
        blood_group: str,
        admission_date: str,
    ) -> None:
        """Initialize a patient.

        Args:
            national_id: The patient's national identification number.
            name: The patient's full name.
            age: The patient's age in years.
            phone: The patient's contact phone number.
            blood_group: The patient's blood group.
            admission_date: The date the patient was admitted.
        """
        super().__init__(national_id, name, age, phone)
        self.__blood_group: str = ""
        self.__admission_date: str = ""
        self.__medical_records: List["MedicalRecord"] = []
        self.__appointments: List["Appointment"] = []

        self.blood_group = blood_group
        self.admission_date = admission_date

    @property
    def blood_group(self) -> str:
        """str: The patient's blood group."""
        return self.__blood_group

    @blood_group.setter
    def blood_group(self, value: str) -> None:
        valid_groups = {"A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"}
        value = str(value).strip().upper()
        if value not in valid_groups:
            raise ValueError(f"blood_group must be one of {sorted(valid_groups)}.")
        self.__blood_group = value

    @property
    def admission_date(self) -> str:
        """str: The date the patient was admitted."""
        return self.__admission_date

    @admission_date.setter
    def admission_date(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("admission_date cannot be empty.")
        self.__admission_date = str(value).strip()

    @property
    def medical_records(self) -> List["MedicalRecord"]:
        """List[MedicalRecord]: A copy of the patient's medical records.

        Read-only: use ``add_medical_record`` to add a new record instead
        of mutating this list directly.
        """
        return list(self.__medical_records)

    @property
    def appointments(self) -> List["Appointment"]:
        """List[Appointment]: A copy of the patient's appointments.

        Read-only: use ``request_appointment`` to add a new appointment
        instead of mutating this list directly.
        """
        return list(self.__appointments)

    def view_info(self) -> str:
        """Return the patient's personal and medical information.

        Returns:
            A formatted string combining the base person info with blood
            group and admission date.
        """
        base = super().view_info()
        return f"{base} | Blood Group: {self.blood_group} | Admission Date: {self.admission_date}"

    def request_appointment(self, appointment: "Appointment") -> None:
        """Add an appointment request to the patient's appointment list.

        Args:
            appointment: The appointment being requested.
        """
        self.__appointments.append(appointment)
        print(f"Appointment (ID: {appointment.appointment_id}) requested successfully")

    def add_medical_record(self, record: "MedicalRecord") -> None:
        """Add a new medical record to the patient's history.

        Args:
            record: The medical record to add.
        """
        self.__medical_records.append(record)
        print(f"Medical Record (ID: {record.record_id}) added")

    def view_history(self) -> None:
        """Print every medical record on file for this patient.

        Prints a friendly message instead if the patient has no records.
        """
        if not self.__medical_records:
            print("No medical records found.")
        else:
            for record in self.__medical_records:
                print(record.view_info())

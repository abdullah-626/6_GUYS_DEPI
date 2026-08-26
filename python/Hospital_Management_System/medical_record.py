"""Module containing the MedicalRecord class."""


class MedicalRecord:
    """Represents a single medical record entry for a patient.

    Private attributes:
        __record_id (str): Unique identifier for this medical record.
        __diagnosis (str): The diagnosis made for the patient.
        __prescription (str): The prescription/treatment given.
        __date (str): The date the record was created.
    """

    def __init__(self, record_id: str, diagnosis: str, prescription: str, date: str) -> None:
        """Initialize a medical record.

        Args:
            record_id: Unique identifier for this medical record.
            diagnosis: The diagnosis made for the patient.
            prescription: The prescription/treatment given.
            date: The date the record was created.
        """
        self.__record_id: str = ""
        self.__diagnosis: str = ""
        self.__prescription: str = ""
        self.__date: str = ""

        self.record_id = record_id
        self.diagnosis = diagnosis
        self.prescription = prescription
        self.date = date

    @property
    def record_id(self) -> str:
        """str: Unique identifier for this medical record."""
        return self.__record_id

    @record_id.setter
    def record_id(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("record_id cannot be empty.")
        self.__record_id = str(value).strip()

    @property
    def diagnosis(self) -> str:
        """str: The diagnosis made for the patient."""
        return self.__diagnosis

    @diagnosis.setter
    def diagnosis(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("diagnosis cannot be empty.")
        self.__diagnosis = str(value).strip()

    @property
    def prescription(self) -> str:
        """str: The prescription/treatment given."""
        return self.__prescription

    @prescription.setter
    def prescription(self, value: str) -> None:
        self.__prescription = str(value).strip()

    @property
    def date(self) -> str:
        """str: The date the record was created."""
        return self.__date

    @date.setter
    def date(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("date cannot be empty.")
        self.__date = str(value).strip()

    def view_info(self) -> str:
        """Return a formatted, multi-line summary of the medical record.

        Returns:
            A string with the record ID, diagnosis, prescription and date,
            each on its own line.
        """
        return (
            f"Record ID: {self.record_id}\n"
            f"Diagnosis: {self.diagnosis}\n"
            f"Prescription: {self.prescription}\n"
            f"Date: {self.date}"
        )

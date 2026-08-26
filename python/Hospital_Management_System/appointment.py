"""Module containing the Appointment class."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Imported only for type checking to avoid circular imports at runtime.
    from patient import Patient
    from doctor import Doctor

_VALID_STATUSES = {"Pending", "Scheduled", "Cancelled"}


class Appointment:
    """Represents an appointment between a patient and a doctor.

    Private attributes:
        __appointment_id (str): Unique identifier for the appointment.
        __date (str): The date of the appointment.
        __time (str): The time of the appointment.
        __status (str): Current status ("Pending", "Scheduled" or "Cancelled").
        __patient (Patient): The patient the appointment is for.
        __doctor (Doctor): The doctor handling the appointment.
    """

    def __init__(
        self,
        appointment_id: str,
        date: str,
        time: str,
        status: str,
        patient: "Patient",
        doctor: "Doctor",
    ) -> None:
        """Initialize an appointment.

        Args:
            appointment_id: Unique identifier for the appointment.
            date: The date of the appointment.
            time: The time of the appointment.
            status: The initial status of the appointment.
            patient: The patient the appointment is for.
            doctor: The doctor handling the appointment.
        """
        self.__appointment_id: str = ""
        self.__date: str = ""
        self.__time: str = ""
        self.__status: str = "Pending"
        self.__patient: "Patient" = patient
        self.__doctor: "Doctor" = doctor

        self.appointment_id = appointment_id
        self.date = date
        self.time = time
        self.status = status

    @property
    def appointment_id(self) -> str:
        """str: Unique identifier for the appointment."""
        return self.__appointment_id

    @appointment_id.setter
    def appointment_id(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("appointment_id cannot be empty.")
        self.__appointment_id = str(value).strip()

    @property
    def date(self) -> str:
        """str: The date of the appointment."""
        return self.__date

    @date.setter
    def date(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("date cannot be empty.")
        self.__date = str(value).strip()

    @property
    def time(self) -> str:
        """str: The time of the appointment."""
        return self.__time

    @time.setter
    def time(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("time cannot be empty.")
        self.__time = str(value).strip()

    @property
    def status(self) -> str:
        """str: Current status ("Pending", "Scheduled" or "Cancelled")."""
        return self.__status

    @status.setter
    def status(self, value: str) -> None:
        if value not in _VALID_STATUSES:
            raise ValueError(f"status must be one of {sorted(_VALID_STATUSES)}.")
        self.__status = value

    @property
    def patient(self) -> "Patient":
        """Patient: The patient the appointment is for (read-only)."""
        return self.__patient

    @property
    def doctor(self) -> "Doctor":
        """Doctor: The doctor handling the appointment (read-only)."""
        return self.__doctor

    def schedule(self) -> None:
        """Mark the appointment as scheduled."""
        self.status = "Scheduled"

    def cancel(self) -> None:
        """Mark the appointment as cancelled."""
        self.status = "Cancelled"

    def view_info(self) -> str:
        """Return a formatted summary of the appointment.

        Returns:
            A string describing the appointment's ID, date, time, status,
            patient and doctor.
        """
        return (
            f"Appointment ID: {self.appointment_id} | Date: {self.date} | "
            f"Time: {self.time} | Status: {self.status} | "
            f"Patient: {self.patient.name} | Doctor: {self.doctor.name}"
        )

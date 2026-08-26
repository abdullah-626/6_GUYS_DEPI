"""Module containing the Hospital class.

The ``Hospital`` class is the top-level container of the whole system:
it owns the departments, patients, staff and appointments and provides
the operations the main program (``main.py``) uses to manage them. All
of its internal collections are private and only reachable through the
methods/properties defined below.
"""

from __future__ import annotations

from typing import List, Optional

from department import Department
from patient import Patient
from staff import Staff
from appointment import Appointment
from medical_record import MedicalRecord


class Hospital:
    """Represents the hospital as a whole.

    Private attributes:
        __name (str): The hospital's name.
        __location (str): The hospital's location/address.
        __departments (List[Department]): Departments belonging to the hospital.
        __patients (List[Patient]): All patients registered at the hospital.
        __staff (List[Staff]): All staff members employed by the hospital.
        __appointments (List[Appointment]): All appointments ever created.
        __next_appointment_id (int): Internal counter used to generate
            appointment IDs.
    """

    def __init__(self, name: str, location: str) -> None:
        """Initialize a hospital.

        Args:
            name: The hospital's name.
            location: The hospital's location/address.
        """
        self.__name: str = ""
        self.__location: str = ""
        self.__departments: List[Department] = []
        self.__patients: List[Patient] = []
        self.__staff: List[Staff] = []
        self.__appointments: List[Appointment] = []
        self.__next_appointment_id: int = 1

        self.name = name
        self.location = location

    # ------------------------------------------------------------------ #
    # Basic properties
    # ------------------------------------------------------------------ #
    @property
    def name(self) -> str:
        """str: The hospital's name."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("name cannot be empty.")
        self.__name = str(value).strip()

    @property
    def location(self) -> str:
        """str: The hospital's location/address."""
        return self.__location

    @location.setter
    def location(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("location cannot be empty.")
        self.__location = str(value).strip()

    @property
    def departments(self) -> List[Department]:
        """List[Department]: A copy of the hospital's departments (read-only)."""
        return list(self.__departments)

    @property
    def patients(self) -> List[Patient]:
        """List[Patient]: A copy of the hospital's patients (read-only)."""
        return list(self.__patients)

    @property
    def staff(self) -> List[Staff]:
        """List[Staff]: A copy of the hospital's staff (read-only)."""
        return list(self.__staff)

    @property
    def appointments(self) -> List[Appointment]:
        """List[Appointment]: A copy of the hospital's appointments (read-only)."""
        return list(self.__appointments)

    # ------------------------------------------------------------------ #
    # Registration
    # ------------------------------------------------------------------ #
    def add_department(self, department: Department) -> None:
        """Register a new department with the hospital.

        Args:
            department: The department to add.
        """
        self.__departments.append(department)
        print(f"Department '{department.name}' added to {self.name} hospital.")

    def add_patient(self, patient: Patient, department_name: Optional[str] = None) -> None:
        """Register a new patient with the hospital.

        Args:
            patient: The patient to add.
            department_name: If provided, the patient is also assigned to
                the department with this name (when it exists).
        """
        self.__patients.append(patient)
        print(f"Patient '{patient.name}' registered at {self.name} hospital.")

        if department_name:
            department = self.find_department(department_name)
            if department:
                department.add_patient(patient)
            else:
                print(f"Note: department '{department_name}' was not found.")

    def add_staff(self, staff_member: Staff, department_name: Optional[str] = None) -> None:
        """Register a new staff member with the hospital.

        Args:
            staff_member: The staff member to add (``Staff``, ``Doctor`` or
                ``Nurse``).
            department_name: If provided, the staff member is also assigned
                to the department with this name (when it exists).
        """
        self.__staff.append(staff_member)
        print(f"Staff '{staff_member.name}' hired at {self.name} hospital.")

        if department_name:
            department = self.find_department(department_name)
            if department:
                department.add_staff(staff_member)
            else:
                print(f"Note: department '{department_name}' was not found.")

    # ------------------------------------------------------------------ #
    # Lookups
    # ------------------------------------------------------------------ #
    def find_department(self, name: str) -> Optional[Department]:
        """Find a department by name (case-insensitive).

        Args:
            name: The department name to search for.

        Returns:
            The matching ``Department``, or ``None`` if not found.
        """
        for department in self.__departments:
            if department.name.lower() == name.lower():
                return department
        return None

    def find_patient(self, national_id: str) -> Optional[Patient]:
        """Find a patient by national ID.

        Args:
            national_id: The national ID to search for.

        Returns:
            The matching ``Patient``, or ``None`` if not found.
        """
        for patient in self.__patients:
            if patient.national_id == national_id:
                return patient
        return None

    def find_staff(self, national_id: str) -> Optional[Staff]:
        """Find a staff member by national ID.

        Args:
            national_id: The national ID to search for.

        Returns:
            The matching ``Staff`` (or subclass) instance, or ``None``.
        """
        for staff_member in self.__staff:
            if staff_member.national_id == national_id:
                return staff_member
        return None

    # ------------------------------------------------------------------ #
    # Appointments & medical records
    # ------------------------------------------------------------------ #
    def schedule_appointment(self, date: str, time: str, patient: Patient, doctor: Staff) -> Appointment:
        """Create, schedule and store a new appointment.

        Args:
            date: The appointment date.
            time: The appointment time.
            patient: The patient the appointment is for.
            doctor: The doctor handling the appointment.

        Returns:
            The newly created ``Appointment`` instance.
        """
        appointment_id = f"A{self.__next_appointment_id:04d}"
        self.__next_appointment_id += 1

        appointment = Appointment(appointment_id, date, time, "Pending", patient, doctor)
        appointment.schedule()

        self.__appointments.append(appointment)
        patient.request_appointment(appointment)

        print(f"Appointment {appointment_id} scheduled for {patient.name} with Dr. {doctor.name}.")
        return appointment

    def cancel_appointment(self, appointment_id: str) -> bool:
        """Cancel an existing appointment by ID.

        Args:
            appointment_id: The ID of the appointment to cancel.

        Returns:
            ``True`` if the appointment was found and cancelled,
            ``False`` otherwise.
        """
        for appointment in self.__appointments:
            if appointment.appointment_id == appointment_id:
                appointment.cancel()
                print(f"Appointment {appointment_id} cancelled.")
                return True
        print(f"Appointment {appointment_id} not found.")
        return False

    def add_medical_record(
        self, patient: Patient, record_id: str, diagnosis: str, prescription: str, date: str
    ) -> MedicalRecord:
        """Create a medical record and attach it to a patient.

        Args:
            patient: The patient the record belongs to.
            record_id: Unique identifier for the record.
            diagnosis: The diagnosis made for the patient.
            prescription: The prescribed treatment.
            date: The date the record was created.

        Returns:
            The newly created ``MedicalRecord`` instance.
        """
        record = MedicalRecord(record_id, diagnosis, prescription, date)
        patient.add_medical_record(record)
        return record

    # ------------------------------------------------------------------ #
    # Reporting
    # ------------------------------------------------------------------ #
    def view_departments(self) -> None:
        """Print a summary of every department in the hospital."""
        if not self.__departments:
            print("No departments found.")
            return
        for department in self.__departments:
            print(department.view_info())

    def view_patients(self) -> None:
        """Print the full info of every patient in the hospital."""
        if not self.__patients:
            print("No patients found.")
            return
        for patient in self.__patients:
            print(patient.view_info())

    def view_staff(self) -> None:
        """Print the full info of every staff member in the hospital."""
        if not self.__staff:
            print("No staff found.")
            return
        for staff_member in self.__staff:
            print(staff_member.view_info())

    def view_appointments(self) -> None:
        """Print the full info of every appointment ever created."""
        if not self.__appointments:
            print("No appointments found.")
            return
        for appointment in self.__appointments:
            print(appointment.view_info())

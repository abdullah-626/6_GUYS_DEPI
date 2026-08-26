"""Module containing the Department class."""

from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from patient import Patient
    from staff import Staff


class Department:
    """Represents a hospital department (e.g. "Cardiology", "Emergency").

    Private attributes:
        __name (str): The department's name.
        __patients (List[Patient]): Patients currently assigned to the department.
        __staff (List[Staff]): Staff members working in the department.
    """

    def __init__(self, name: str) -> None:
        """Initialize a department.

        Args:
            name: The department's name.
        """
        self.__name: str = ""
        self.__patients: List["Patient"] = []
        self.__staff: List["Staff"] = []

        self.name = name

    @property
    def name(self) -> str:
        """str: The department's name."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not str(value).strip():
            raise ValueError("name cannot be empty.")
        self.__name = str(value).strip()

    @property
    def patients(self) -> List["Patient"]:
        """List[Patient]: A copy of the patients assigned to this department.

        Read-only: use ``add_patient`` to assign a patient instead of
        mutating this list directly.
        """
        return list(self.__patients)

    @property
    def staff(self) -> List["Staff"]:
        """List[Staff]: A copy of the staff assigned to this department.

        Read-only: use ``add_staff`` to assign a staff member instead of
        mutating this list directly.
        """
        return list(self.__staff)

    def add_patient(self, patient: "Patient") -> None:
        """Assign a patient to this department.

        Args:
            patient: The patient to add.
        """
        self.__patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")

    def add_staff(self, staff_member: "Staff") -> None:
        """Assign a staff member to this department.

        Args:
            staff_member: The staff member to add.
        """
        self.__staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")

    def find_staff(self, national_id: str) -> Optional["Staff"]:
        """Look up a staff member in this department by national ID.

        Args:
            national_id: The national ID to search for.

        Returns:
            The matching staff member, or ``None`` if not found.
        """
        for staff_member in self.__staff:
            if staff_member.national_id == national_id:
                return staff_member
        return None

    def view_info(self) -> str:
        """Return a short summary of the department (name + head counts).

        Returns:
            A formatted string with the department name and the number
            of patients and staff assigned to it.
        """
        return (
            f"Department: {self.name} | Patients: {len(self.__patients)} | "
            f"Staff: {len(self.__staff)}"
        )

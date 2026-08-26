"""Entry point of the Hospital Management System.

Running this module starts an interactive, menu-driven console
application that lets the user:
    - Create the hospital.
    - Add departments, patients, doctors and nurses.
    - Schedule / cancel appointments.
    - Add and view patients' medical records.
    - View departments, patients, staff and appointments.
"""

from __future__ import annotations



from hospital import Hospital
from department import Department
from patient import Patient
from doctor import Doctor
from nurse import Nurse
from staff import Staff


# ---------------------------------------------------------------------- #
# Small input helpers (keep the menu loop below readable & crash-proof)
# ---------------------------------------------------------------------- #
def read_int(prompt: str) -> int:
    """Keep asking the user until a valid integer is entered.

    Args:
        prompt: The message shown to the user.

    Returns:
        The integer value entered by the user.
    """
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid whole number.")


def read_float(prompt: str) -> float:
    """Keep asking the user until a valid float is entered.

    Args:
        prompt: The message shown to the user.

    Returns:
        The float value entered by the user.
    """
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")


def read_non_empty(prompt: str) -> str:
    """Keep asking the user until a non-empty string is entered.

    Args:
        prompt: The message shown to the user.

    Returns:
        The trimmed, non-empty string entered by the user.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


# ---------------------------------------------------------------------- #
# Menu
# ---------------------------------------------------------------------- #
def show_menu() -> None:
    """Print the main menu of the application."""
    print("\n" + "=" * 40)
    print("      HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1.  Add Department")
    print("2.  Add Patient")
    print("3.  Add Doctor")
    print("4.  Add Nurse")
    print("5.  Schedule Appointment")
    print("6.  Add Medical Record")
    print("7.  View Departments")
    print("8.  View Patients")
    print("9.  View Staff")
    print("10. View Appointments")
    print("11. View a Patient's Medical History")
    print("12. Cancel Appointment")
    print("13. Exit")


# ---------------------------------------------------------------------- #
# Menu actions
# ---------------------------------------------------------------------- #
def handle_add_department(hospital: Hospital) -> None:
    """Prompt for a department name and add it to the hospital."""
    name = read_non_empty("Enter department name: ")
    hospital.add_department(Department(name))


def handle_add_patient(hospital: Hospital) -> None:
    """Prompt for patient details and register the patient."""
    national_id = read_non_empty("Enter national ID: ")
    name = read_non_empty("Enter patient name: ")
    age = read_int("Enter age: ")
    phone = read_int("Enter phone number: ")
    blood_group = read_non_empty("Enter blood group (e.g. O+): ")
    admission_date = read_non_empty("Enter admission date (YYYY-MM-DD): ")

    patient = Patient(national_id, name, age, phone, blood_group, admission_date)

    department_name = input("Assign to department (leave empty to skip): ").strip()
    hospital.add_patient(patient, department_name or None)


def handle_add_doctor(hospital: Hospital) -> None:
    """Prompt for doctor details and hire the doctor."""
    national_id = read_non_empty("Enter national ID: ")
    name = read_non_empty("Enter doctor name: ")
    age = read_int("Enter age: ")
    phone = read_int("Enter phone number: ")
    employee_id = read_non_empty("Enter employee ID: ")
    joining_date = read_non_empty("Enter joining date (YYYY-MM-DD): ")
    specialty = read_non_empty("Enter specialty: ")
    consultation_fee = read_float("Enter consultation fee: ")
    license_number = input("Enter license number (optional): ").strip()

    doctor = Doctor(
        national_id, name, age, phone, employee_id, joining_date,
        specialty, consultation_fee, license_number,
    )

    department_name = input("Assign to department (leave empty to skip): ").strip()
    hospital.add_staff(doctor, department_name or None)


def handle_add_nurse(hospital: Hospital) -> None:
    """Prompt for nurse details and hire the nurse."""
    national_id = read_non_empty("Enter national ID: ")
    name = read_non_empty("Enter nurse name: ")
    age = read_int("Enter age: ")
    phone = read_int("Enter phone number: ")
    employee_id = read_non_empty("Enter employee ID: ")
    joining_date = read_non_empty("Enter joining date (YYYY-MM-DD): ")
    shift = read_non_empty("Enter shift (Morning/Evening/Night): ")
    certifications = input("Enter certifications (optional): ").strip()

    nurse = Nurse(
        national_id, name, age, phone, employee_id, joining_date,
        shift, certifications,
    )

    department_name = input("Assign to department (leave empty to skip): ").strip()
    hospital.add_staff(nurse, department_name or None)


def handle_schedule_appointment(hospital: Hospital) -> None:
    """Prompt for a patient and doctor ID, then schedule an appointment."""
    if not hospital.patients or not hospital.staff:
        print("You need at least one patient and one staff member first.")
        return

    patient_id = read_non_empty("Enter patient national ID: ")
    patient = hospital.find_patient(patient_id)
    if not patient:
        print("Patient not found.")
        return

    doctor_id = read_non_empty("Enter doctor national ID: ")
    doctor = hospital.find_staff(doctor_id)
    if not doctor:
        print("Staff member not found.")
        return

    date = read_non_empty("Enter appointment date (YYYY-MM-DD): ")
    time = read_non_empty("Enter appointment time (HH:MM): ")

    hospital.schedule_appointment(date, time, patient, doctor)


def handle_add_medical_record(hospital: Hospital) -> None:
    """Prompt for a patient ID and record details, then save the record."""
    patient_id = read_non_empty("Enter patient national ID: ")
    patient = hospital.find_patient(patient_id)
    if not patient:
        print("Patient not found.")
        return

    record_id = read_non_empty("Enter record ID: ")
    diagnosis = read_non_empty("Enter diagnosis: ")
    prescription = read_non_empty("Enter prescription: ")
    date = read_non_empty("Enter date (YYYY-MM-DD): ")

    hospital.add_medical_record(patient, record_id, diagnosis, prescription, date)


def handle_view_patient_history(hospital: Hospital) -> None:
    """Prompt for a patient ID and print their medical history."""
    patient_id = read_non_empty("Enter patient national ID: ")
    patient = hospital.find_patient(patient_id)
    if not patient:
        print("Patient not found.")
        return
    patient.view_history()


def handle_cancel_appointment(hospital: Hospital) -> None:
    """Prompt for an appointment ID and cancel it."""
    appointment_id = read_non_empty("Enter appointment ID: ")
    hospital.cancel_appointment(appointment_id)


def create_hospital() -> Hospital:
    """Prompt for the hospital's name and location, then create it.

    Returns:
        The newly created ``Hospital`` instance.
    """
    name = read_non_empty("Enter hospital name: ")
    location = read_non_empty("Enter hospital location: ")
    hospital = Hospital(name, location)
    print("\nHospital created successfully!")
    return hospital


# ---------------------------------------------------------------------- #
# Main loop
# ---------------------------------------------------------------------- #
def main() -> None:
    """Run the interactive Hospital Management System."""
    hospital = create_hospital()

    actions = {
        "1": handle_add_department,
        "2": handle_add_patient,
        "3": handle_add_doctor,
        "4": handle_add_nurse,
        "5": handle_schedule_appointment,
        "6": handle_add_medical_record,
        "7": lambda h: h.view_departments(),
        "8": lambda h: h.view_patients(),
        "9": lambda h: h.view_staff(),
        "10": lambda h: h.view_appointments(),
        "11": handle_view_patient_history,
        "12": handle_cancel_appointment,
    }

    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "13":
            print(f"\nThank you for using {hospital.name} Hospital Management System. Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice, please try again.")
            continue

        try:
            action(hospital)
        except Exception as error:  # keep the menu alive on unexpected input errors
            print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()

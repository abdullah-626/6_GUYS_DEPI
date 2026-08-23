from staff import Staff

class Doctor(Staff):
    def _init_(self, national_id: str, name: str, age: int, phone: int, 
                 employee_id: str, joining_date: str, specialty: str, 
                 consultation_fee: float, license_number: str = ""):

        super()._init_(national_id, name, age, phone, employee_id, joining_date)
        
        self.specialty = specialty
        self.consultation_fee = consultation_fee
        self.license_number = license_number

    def prescribe_medicine(self, patient, medicine_details: str):
        print(f"Doctor {self.name} prescribed: {medicine_details} for Patient {patient.name if hasattr(patient, 'name') else patient}")

    def examine_patient(self, patient) -> None:
        print(f"Doctor {self.name} is examining patient: {patient.name if hasattr(patient, 'name') else patient}")

    def view_info(self) -> str:
        base_info = super().view_info()
        return (f"{base_info} | Specialty: {self.specialty} | "
                f"Fee: {self.consultation_fee} | License: {self.license_number}")
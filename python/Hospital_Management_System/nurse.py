from staff import Staff

class Nurse(Staff):
    def __init__(self, national_id: str, name: str, age: int, phone: int, 
                 employee_id: str, joining_date: str, shift: str, 
                 certifications: str = ""):
        super().__init__(national_id, name, age, phone, employee_id, joining_date)

        self.shift = shift  
        self.certifications = certifications

    def take_vitals(self, patient) -> None:
        print(f"Nurse {self.name} is taking vitals for patient: {patient.name if hasattr(patient, 'name') else patient}")

    def view_info(self) -> str:
        base_info = super().view_info()
        return f"{base_info} | Shift: {self.shift} | Certifications: {self.certifications}"
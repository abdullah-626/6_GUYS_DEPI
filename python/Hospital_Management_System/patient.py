from person import Person

class Patient(Person):
    def __init__(self, national_id:str, name:str, age:int, phone:int, blood_group:str, admission_date:int):
        super().__init__(national_id, name, age, phone)
        self.blood_group = blood_group
        self.admission_date = admission_date
        self.medical_records = [] 
        self.appointments = []

    def view_info(self):
        base = super().view_info()
        return f"{base} | Blood Group: {self.blood_group} | Admission Date: {self.admission_date}"
    
    def request_appointment(self,appointment):
        self.appointments.append(appointment)
        print(f"Appointment (ID: {appointment.appointment_id}) requested successfully")

    def add_medical_record(self, record):
        self.medical_records.append(record)
        print(f"Medical Record (ID: {record.record_id}) added")

    def view_history(self):
        if not self.medical_records:
            print("No medical records found.")
        else:
            for record in self.medical_records:
                print(record.view_info())

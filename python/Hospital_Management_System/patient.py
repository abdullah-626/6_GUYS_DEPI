from person import Person

class Patient(Person):
    def __init__(self, national_id, name, age, phone, blood_group:str, admission_date:int):
        super().__init__(national_id, name, age, phone)
        self.blood_group = blood_group
        self.admission_date = admission_date
        self.medical_records = [] 
        self.appointments = []

    def view_info(self):
        return f""" national id is: {self.national_id}\n name is: {self.name}\n age is: {self.age}
 phone number is: {self.phone} \n blood group is: {self.blood_group}
"""
    def request_appointment(self):
        pass
    def view_history(self):
        pass
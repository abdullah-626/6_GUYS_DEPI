from person import Person

class Staff(Person):
    def __init__(self, national_id, name, age, phone, employee_id:str, joining_date:int):
        super().__init__(national_id, name, age, phone)
        self.employee_id = employee_id
        self.joining_date = joining_date

    def view_info(self):
        return super().view_info()

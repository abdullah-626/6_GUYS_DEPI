class Department:

    def _init_(self, name):
        self.name = name
        self.patients = []
        self.staff = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")
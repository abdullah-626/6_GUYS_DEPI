class MedicalRecord:
    def __init__(self,record_id,diagnosis,prescription,date):
        self.record_id=record_id
        self.diagnosis=diagnosis
        self.prescription=prescription
        self.date=date
    def view_info(self):
        return (
            f"Record ID: {self.record_id}\n"
            f"Diagnosis: {self.diagnosis}\n"
            f"Prescription: {self.prescription}\n"
            f"Date: {self.date}"
        )
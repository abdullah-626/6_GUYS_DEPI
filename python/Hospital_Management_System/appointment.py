class Appointment:
    def __init__(self,appointment_id,date,time,status,patient,doctor):
        self.appointment_id=appointment_id
        self.date=date
        self.time=time
        self.status=status
        self.patient=patient
        self.doctor=doctor
    def schedule(self):
        self.status="Scheduled"
    def cancel(self):
        self.status="Cancelled"

from abc import ABC, abstractmethod

class Person (ABC):
    @abstractmethod
    def __init__(self, national_id:str, name:str, age:int, phone:int):
        self.national_id = national_id
        self.name = name
        self.age = age
        self.phone = phone
    def view_info(self) -> str:
        return f"National ID: {self.national_id} | Name: {self.name} | Age: {self.age} | Phone: {self.phone}"



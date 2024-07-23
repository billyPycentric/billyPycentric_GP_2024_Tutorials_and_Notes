import logging
from dataclasses import dataclass

logging.basicConfig(filename='emp.log',level=logging.INFO,format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')



@dataclass
class Employee:
    names: str
    surname: str
    email:str
    years_with_company:int
    

    def emp_info(self,names,surname,email,years_with_company):
        logging.info(f"The employee {self.names} was CREATED")
        return (f"The employees name is {self.names} and surname is{self.surname} and email: {self.email} they have been working for {self.years_with_company}")



emp1 = Employee("Abongile","billy","abobilly@gmail.com",5)
print(emp1.emp_info)
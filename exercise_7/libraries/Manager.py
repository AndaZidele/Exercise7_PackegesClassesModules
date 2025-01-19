import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from libraries.Employee import Employee
from libraries.Roles import Roles

class Manager(Employee):

    salary = None
    countOfSubordinates = None

    def setSalary(self, salary):
        self.salary = salary

    def getCountOfSubordinates(self, countOfSubordinates):
        return self.countOfSubordinates
    
manager1 = Manager("Dace", "Dacite", 34)
manager1.setDescription(Roles.EMPLOYEE, "Bachelor in Sales Management", 8)
manager1.setInfoAboutThisJob("Sales manager", 3)
manager1.setInfoAboutPreviousExperience(["Administrator", "Subordinate in Sales department"])
print(manager1.getPersonsInformation())
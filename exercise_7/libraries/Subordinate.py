import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from libraries.Employee import Employee
from libraries.Roles import Roles

class Subordinate(Employee):
    salary = None

    def setSalary(self, salary):
        self.salary = salary

subordinate1 = Subordinate("Aldis", "Aldins", 26) # no klases "Person" (inicializacijas funkcija _init_)
subordinate1.setDescription(Roles.EMPLOYEE, "Bachelor degree in IT", 2)
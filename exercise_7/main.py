import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("Subordinate"), '..', 'libraries')))

from libraries import Roles
from libraries import Person
from libraries import Employee
from libraries import Subordinate
from libraries import Manager

# Palaižot šo programmu izvadās informācija, kas prasīta šajā failā ("main.py"), un arī informācija no visām importētajām klasēm:
# No klases "Manager" izvadās personas informācija (tajā klasē ir prasīts, lai to izvada)
# klasē Subordinate ir izveidots objekts, kas tiek izvadīts šajā klasē
# Būtībā no šīs klases var piekļūt jebkuras importētās klases funkcijām un tajās izveidotajiem objektiem.

try:
    manager2 = Manager.Manager("Juris", "Juritis", 44)
    manager2.setDescription(Roles.Roles.EMPLOYEE, "Bachelor in Sales Management", 18)
    manager2.setInfoAboutThisJob("Sales manager", 13)
    manager2.setInfoAboutPreviousExperience(["Subordinate in Sales department"])

    print(manager2.getPersonsInformation()) # izvada personas informācija
    print(manager2.getPersonsExperience()) # izvada informāciju par darba pieredzi

    print(Subordinate.subordinate1.getPersonsInformation()) # objekt no klases Subordinate tiek šeit izvadīts

except ZeroDivisionError as ex:
    print("Exceptions was: ", ex)

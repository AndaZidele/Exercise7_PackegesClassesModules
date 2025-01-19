import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from libraries.Person import Person

class Employee(Person):

    nameOfPosition = ""
    inThisPosition = None
    previousJobsTitles = []

    def setInfoAboutThisJob(self, nameOfPosition, inThisPosition):
        self.nameOfPosition = nameOfPosition
        self.inThisPosition = inThisPosition

    def setInfoAboutPreviousExperience(self, previousJobsTitles):
        self.previousJobsTitles = previousJobsTitles
        self.previousJobsTitles.sort()

    def getPersonsExperience(self):
        return """
            --- Work Experience ---
            Current job: {}
            Experience of working in this position: {}
            Previous jobs: {}
        """.format(self.nameOfPosition, self.inThisPosition, self.previousJobsTitles)
    

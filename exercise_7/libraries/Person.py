class Person(object):

    fname = ""
    lname = ""
    age = None
    role = None
    education = ""
    jobExperience = None

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def setDescription(self, role, education, jobExperience):
        self.role = role
        self.education = education
        self.jobExperience = jobExperience

    def getPersonsInformation(self):
        return """
            --- PERSON ---
            firstname: {}
            lastname: {}
            age: {}
            role: {}
            education: {}
            jobExperience : {}
        """.format(self.fname, self.lname, self.age, self.role, self.education, self.jobExperience)
    
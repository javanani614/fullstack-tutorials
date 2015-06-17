class Test(object):
    """This class will create a new test"""
    score = 0
    
    
    def __init__(self, score=None):
        
        if score != None:
            if score in range(1, 100):
                self.score = score
            else:
                raise Exception ('invalid score')

    def printTest(self):
        print "the score = " + str(self.score) 

test = Test(40)
test.printTest()
   
class Student(object):
    """This class will create a new student"""
    name = ""
    testList = []
    )
        
    def __init__(self, name=None, test=None):
        
        if self.name  != None:
            self.name = name
        else:
            self.name = "Jane Doe"

        ##self.tests.append = testTest(75))         

    def printStudent(self):
        print self.name + " " 
        print self.testList

student = Student("Lauren")
student.printStudent()

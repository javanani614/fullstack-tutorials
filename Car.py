class Car(object):
    """This class will create a new car"""
    make = ""
    model = ""
    year = 0
    
    def __init__(self, make=None, model=None, year=None):
        if make != None:
           self.make = make
        else:
           self.make = "generic make"
    
        if model != None:
           self.model = model
        else:
            self.model = "generic model"  
        
        if self.year != None:
            self.year = year
        else:
            self.year = 1900

    def printDetails(self):
        print self.make + " " + self.model + " " + str(self.year)
    
new_car = Car()
new_car.printDetails()
new_car2 = Car("Toyota")
new_car2.printDetails()
new_car3 = Car("Honda", "Civic")
new_car3.printDetails()
new_car3 = Car("Porsche", "Civic", 2015)
new_car3.printDetails()







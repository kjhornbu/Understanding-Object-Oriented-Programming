# We are defining a car object
#upper class is for classes because they are propernames #colon is new line and begin indentation
#don't have to import other classes together
from driver import Driver
class Car:
    def __init__(self,driver=None,make="Ford",model="F150",year="2000"): #need to set as init because it is basically the starting conditiosn of the class
        self.make=make
        self.model=model
        self.year=year
        self.fuel=100
        self.miles=0
        self.driver=driver
        #self term is talking about that specific instance of that object
        #you don't have to put all attributes into init!
        
        
    def description(self):
        #for multiple line printing use """ """
        print(f""" 
        Make: {self.make}
        Model: {self.model}
        Year: {self.year}
        Fuel: {self.fuel}
        """)
        self.driver.description()
        
    @staticmethod
    def are_cool():
        print("Yeah!")
        
    def drive(self,miles_driven):
        #increase milaage on the car and decrease the fuel
        
        #check fuel level
        if self.fuel==0:
            print("Out of Fuel :(")
        elif miles_driven>self.fuel:
            print("Out of Fuel :(")
            self.miles=self.miles+self.fuel
            self.driver.log_miles(self.fuel)
            self.fuel=0
        else:
            self.miles=self.miles+miles_driven # you can redefine attributes with things in the class
            self.fuel=self.fuel-miles_driven
            self.driver.log_miles(miles_driven)#log the miles driven in another class
    
    def top_off(self):
        self.fuel=100
        
        
        
        
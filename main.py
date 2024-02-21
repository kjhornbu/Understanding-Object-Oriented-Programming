from car import Car
from driver import Driver

#car = Car("","Ford","F150","1999")
#print(dir(car))

#print("++++++++++++++++++++++++++++++")

#print(f"The make is {car.make}")
#print(f"The model is {car.model}")
#print(f"The year is {car.year}")

#print("++++++++++++++++++++++++++++++")

#car_2 = Car("kia","sorento","2024")
#print(f"The make is {car_2.make}")
#print(f"The model is {car_2.model}")

#with self.self then you have car car... so dont' do this self.self=Car in very chicken egg situtation want to be able to read the code later on

#print("++++++++++++++++++++++++++++++")

driver=Driver()
#driver.description()

car_3 = Car(driver=driver)
car_3.description()

#how many attributes on initalization? 

#after making a bunch of attirubtes should you make engine attributes then after awhile should you make a engine class. 
#print("++++++++++++++++++++++++++++++")

#car.description #description is a function and you didn't invoke it.
#car.description()#handled the print in the decription there


## Now lets drive the car
print("++++++++++++++++++++++++++++++")
car_3.drive(120)
car_3.description()
driver.are_cool()
car_3.are_cool()

## Now lets top off the gas for the car
print("++++++++++++++++++++++++++++++")
car_3.top_off()
car_3.description()
#driver.description()



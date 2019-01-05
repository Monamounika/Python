class Car:
    wheels = 4 #Static(Class) Variable
    def __init__(self):
        self.com = "BMW"
        self.mil = 8
c1 = Car()
c2 = Car()

c1.mil=50

Car.wheels = 6
print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,Car.wheels)

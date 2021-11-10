class Bicycle:
    
    gear = 0
    speed = 0
    
    def __init__(self, _gear = 0, _speed = 0):
        self.gear = _gear
        self.speed = _speed

    def brake(self, decrement = 0):
        self.speed -= decrement

    def speedUp(self, increment = 0):
        self.speed += increment

    def info(self):
        print('Speed is {}\n Gear is {}'.format(self.speed, self.gear))

# Mountain Bike derived from Bicycle
class mountainBike(Bicycle):
    seat = 0

    def __init__(self, _gear, _speed, height = 0):
        super().__init__(_gear, _speed)
        self.seat = height

    def info(self):
        print('Speed is {}\n Gear is {} \n Seat height {}'.format(self.speed, self.gear, self.seat))

obj1 = mountainBike(3,10,2)
obj2 = Bicycle(4,10)

print('Current information on the mountain bike: ')
obj1.info()
print('Current information of the bike is: ')
obj2.info()

obj1.speedUp(2)

obj2.brake(3)

print('After updating the speed')
print('Mountain bike information is: ')
obj1.info()
print('Bike information is: ')
obj2.info()
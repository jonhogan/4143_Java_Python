class Bicycle:
    
    gear = 0
    speed = 0
    
    def init(self, g = 0, s = 0):
        self.gear = g
        self.speed = s

    def brake(self, decrement=None):
        self.speed-=decrement

    def speedUp(self, increment=None):
        self.speed+=increment

    def status(self):
        print(f'Speed is {self.speed}\n Gear is {self.gear}')

# Mountain Bike inh. from Bicycle
class mountainBike(Bicycle):
    seatHeight=int()

    def init(self, g = 0, s = 0, sh = 0):
        super().init(g,s)
        self.seatHeight = sh

    def status(self):
        print(f'Speed is {self.speed}\n Gear is {self.gear} \n seat Height {self.seatHeight}')

# Make an objects for Bike and Mountain Bike
mb1 = mountainBike(2,26,3)
bik1 = Bicycle(5,66)

# Get the status before
print('the Status before changing speed')
print('Mountain status is: ')
mb1.status()
print('Bicycle Bike status is: ')
bik1.status()

# Speed Up my mountain bike by 4 mph
mb1.speedUp(4)

# Brake up my car by 6 mph
bik1.brake(6)

# Get the status after
print('the Status after changed the speed')
print('Mountain status is: ')
mb1.status()
print('Bicycle Bike status is: ')
bik1.status()
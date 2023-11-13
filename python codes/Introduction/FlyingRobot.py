# now we want to create another specific type of robots like a flying robot that will inherit from the Robot class

# frist we import Robot class from Robot.py

from Robot import Robot

class FlyingRobot(Robot):
    def __init__(self,name,DOFs,max_altitude):
        super().__init__(name,DOFs)
        self.max_altitude = max_altitude

    def move(self):
        print(f'I am a flying robot with a max altitude of {self.max_altitude}')
        super().move() #we inherit the move method from the base class



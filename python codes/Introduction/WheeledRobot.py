#now we want to create specific types of robots as a wheeled robot that can inherit from the base robot class
#this means that from Robot.py we import the Robot class

from Robot import Robot

class WheeledRobot(Robot):
    def __init__(self,name,DOFs,num_wheels):
        super().__init__(name,DOFs) #here we inherited the (initialization) function from the base Robot class
        self.num_wheels = num_wheels
    
    def move(self):
        print(f'I am a wheeled robot with {self.num_wheels} wheels')
        super().move() #here we called the move method from the base class


    
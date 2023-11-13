class Robot:
    def __init__ (self,name,DOFs):
        self.name = name
        self.DOFs = DOFs

    def introduce(self):
        print(f'I am {self.name}, a {self.DOFs} DOF robot.')

    def move(self):
        print('I can move.')


#in this Robot class, we have defined an init method to initialize the name and the DOF of the robot
#an introduce method to introduce the robot
#A move method to indicate that the robot can move

### INHERITANCE CONTINUED ##

# now if we want to create specific types of robots, such as wheeled robot and flying robot, that inherit from the base Robot Class
#We have the classes as follows
#See WheeledRobot.py and FlyingRobot.py


# A class 'Robot' where each robot is identified by its 'name' and it has 2 methods
# introduce method - should pront the robots name
# remove method - should decrease the number of robots and print an appropriate message on whether there are any active robots left
# The class should keep track of the total number of active robots (i.e the robots that have been created)
# should have a class method that prints the number of active robots
num_of_robs = []
class Robot():
    def __init__(self, name):
        self.name = name
        num_of_robs.append(self.name)


    def introduce(self):
        print(f'Hi! I am {self.name}')
        
    def number_active_robots():
        print('There are ' + str(len(num_of_robs)) + ' active robots')

    def remove(self):
        num_of_robs.remove(self.name)
        



robot1 = Robot('R1')
robot1.introduce()
Robot.number_active_robots()

robot2 = Robot('R2')
robot2.introduce()
Robot.number_active_robots()

robot1.remove()

robot3 = Robot('R3')
robot3.introduce()
Robot.number_active_robots()

robot2.remove()
robot3.remove()

Robot.number_active_robots()


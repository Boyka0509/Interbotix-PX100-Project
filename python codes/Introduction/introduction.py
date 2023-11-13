print('hello adi how are you doing')

#DATA TYPES IN PYTHON
num_int = 10 #integer
print(num_int)

num_float = 1.25 #float
print(num_float)

#BASIC ARITHMETICS
print(num_int + (num_int + (num_float)**2))
print((num_int)**(num_float))


#DIFFERENT MSTH FUNCTION
print(max(num_int, 9)) # max gives us the max number in our list
print(min(num_float,1)) # min gives us the min number in the list
print(abs(-num_int)) # abs gives us the absolute value of the number
print(pow(num_int,2)) # pow gives us the the first number to the power of the second number
print(round(num_float)) # roun gives us the the option to round the number either up or down


#There are some other math functions that needs to be imported from the 'module' to use them 
from math import * # This means that now we can use all the functions from the math library without having to prefix them like usually we do 'math.add' and so on
#some funstions that are in the math library
print(floor(num_float)) # floor will chop the decimal point
print(ceil(num_float))  # ceil will round the number up print(sqrt(num_int**num_float)) #sqrt will give us the square root

#we can also import a library as a preferred name for simplicity for example 'import math as m' and use the functions within the library like so 'm.exp(num_int)'

#Combining strings
print('There are ' + str(num_int) + ' arms  robots in the factory and 1 of them is broken')

#PLAYING WITH STRINGS

#assigning a string to a variable
factory_name = 'VAS'
print('The factory name is ' + factory_name)

#accessing the letters of the string using indexes []
print('The first character in the factory name is ' + factory_name[0])
print('The second character in the factory name is ' + factory_name[2])

#Different functions to play with strings
print(factory_name.lower()) #lower() will change all the characters of the string to lower case
print(factory_name.islower()) #islower will check if the string characters is in lower case
print(factory_name.upper().isupper())#upper() will change the characters of the string to upper case and the isupper() will check if the characters are in upper case
print(len(factory_name)) #len() will give us the length of the striong
print(factory_name[0:len(factory_name)-1]) # we can access individual characters using [] notations, in this example the characters from the first character upto one to the last character will be spit out
print(factory_name.index('A')) # .index() will help us know where a specific character is
print(factory_name.replace('VAS','ADI')) # .replace() function will replace the string from the first one being the thing string that you want to replace and the second string that you wanted it to be replaced with

### LISTS ###
#used to store numbers, strings, objects or any other type of data

robot_brands = ['ABB', 'KUKA', 'FANUC', 'OMRON', 'KAWASAKI'] # this creates a list of 'robot brands' that manufactures robots

#access the items in the list using the indes
print(robot_brands[2]) #prints out the 3rd item in the list, i.e FANUC

#using slices we can acces a range of items from the list
print(robot_brands[:4]) # this prints out the items from 0 to 4th item

#adding an item to the list can be done by .append()
robot_brands.append('UR')
print(robot_brands)

#an item can be removed from the list using the .remove()
robot_brands.remove('UR')
print(robot_brands)

#an item can be inserted into the lilst at a specific index number using .insert()
robot_brands.insert(0,'UR')
print(robot_brands)

#we can sort the list using the .sort()
robot_brands.sort()
print(robot_brands)

#we can reverse the order of the items in the list using the .reverse()
robot_brands.reverse()
print(robot_brands)

#length of the list can be found using the .len()
print(len(robot_brands))

#we can add or a list to another list using the extend funstion
robot_brands1 = ['yaskawa','stabuli']
robot_brands.extend(robot_brands1)
print(robot_brands)

#to get rid of the last element on the list we use pop function
robot_brands.pop()
print(robot_brands)

#to know the index of a certain value or item in the list we can use .index()
print(robot_brands.index('ABB'))

#to count the number of times a value or item is repeated in the list we use the .count()
print(robot_brands.count('ABB'))

#to make a copy of the list we use the .copy()
robot_brands2 = robot_brands.copy()
print(robot_brands)
print(robot_brands2)

#a for loop can be used to iterate through the list, in the below example the for loop iterates through the list and prints out each value in the list
for robot_brand in robot_brands:
    print(robot_brand)
    
#we can remove everything using the .clear() function
robot_brands.clear()


#### 2D LISTS ####
#it is also known as a nested list
#allows us to create a grid like structure where each element represents a row and a coloumn

matrix = [[1,2,3],[4,5,6],[7,8,9]] #this creates a 3x3 matrix with the elements

#we can access the elements of the matrix by specifying the index numbers
print(matrix[0][0]) #prints the element in the first row in the first column
print(matrix[1][1]) #this will print 5

#we can also modify an elemnt in the 2D list like so
matrix[2][2] = 10
print(matrix[2][2])

#2D lists are useful for representing grids, table and marices in python


### TUPLES ###
#similar to lists but they are immutable

#the following code creates a tuple of robotics engineers in the factory
robotic_engineers = ('Aditya','Boyka','Jawa','Adi')

#tuples can be indexed and sliced just like lists
print(robotic_engineers[2])

#can also be unoacked into multiple variables, for example the code below unpackes the tuple into the variables e1, e2, e3, e4
e1, e2, e3, e4 = robotic_engineers
print(e1,e2,e3,e4)
print(e1)

# can be used to store any type of data, strings, numbers, lists and other tuples
# often used to store data that does not need to be changed, such as the names of ppl in a group and/or the coordinate points on a map
#we can change anythin in a tuple unlike lists it will spit out an error
#robotic_engineers[1] = 'bob'  # this spits a type error, tuple object does not support item assignment

#we can make a ;list' of 'tuples like so
robot_businesses = [('adi','jawa'),('mallige','raj')]
print(robot_businesses)

#### DICTIONARIES #####

# A data structure that stores data in key-value pairs
#can create these pairs and when we wante to access the infor, we can refer it by its keys.
#keys are uniwue, not be repeated, case sensitive, and can be any immutable type, such as strings, numbers or tuples. 
#can access the values via keys

#create a dictionary in python, we must enclose a sequence of elemtnts inside curly brackets and seperate them with commas

#Example 1

object_colors = {'ball':'red', 'cube': 'green', 'flower':'pink', 'pyramid':'blue'}
print('The cube is ' + object_colors['cube'])
print('The ball is ' + object_colors['ball'])

#we can also use .get() to retrieve the value associatewd with a key
print(object_colors.get('cubee', 'no such object'))


## EXAMPLE 2

# We create a dictionary for a robot with 3 revolute joints and its dictionary has three keys
# The keys will be Jint 1, Joint 2, Joint 3
# Eache key has minimum angle, maximum angle, and the default angle
# Min and max defin the range of motion of the revolute joint
# Default angle is the angle that the joint is set to when the robot arm is first turned on (may be the home pos)

import math as m

arm_dict = { 

    'joint 1' : {
        'min' : -m.pi/2,
        'max' : m.pi/2,
        'default' : 0,
    },

    'joint 2' : {
        'min' : -m.pi,
        'max' : m.pi,
        'default': 0,
    },

    'joint 3' : {
        'min': -m.pi/2,
        'max': m.pi/2,
        'default' : 0,
    },
}

#now we can access the keys and values in this dictionary 
joint_angles_1 = arm_dict['joint 1']
print(joint_angles_1)

#I can also access the individual angles within each joint in the dictionary
print(arm_dict['joint 1']['max'])

#min angle of joint3
print(arm_dict['joint 3']['min'])

#default angle of joint2
print(arm_dict['joint 2']['default'])



### FUNCTIONS AND RETURN STATEMENTS ####

# A function is a block of code that performs a specific task
#the return statement is used to exit a function and return a vlue to the calles
# the value that is returned can be any python object

#Basic Example of a simple function
def add(a,b):
    return a+b

print(add(3,4))

#Example 2 - a function that gets the radius of the wheel of the robot and returns the wheel area
def cal_wheel_area(radius):
    area = m.pi * radius**2
    return area

wheel_radius = 8
print(cal_wheel_area(wheel_radius))


### Conditional Statements: if statements ###

# 1. If (else) statement
#it is a conditional statement
#allows to execute certain blocks of code based on whether a specified condition is true or false

# EXAMPLE 1
# we want to control a two-joint robot arm with a joystick
#if the joystick is tilted to the right --> 1st joint rotates in + direction based on RHR
# if the joystick is tilted to the left --> 1st joint rotates in - direction based on RHR
# if the joystick is tilted up --> 2nd joint rotates in + direction based on RHR
# if the joystick is tilted down --> 2nd joint rotates in - direction based on RHR
# in neutral position --> the arm does not move

#we first get the input (now this can be done so that you can get the input from an actual joystick, for example on the tello drone)
joystick_in = 'right'

if joystick_in == 'right':
    print('moving the 1st joint in the positive direction')
elif joystick_in == 'left':
    print('moving 1st joint in megative direction')
elif joystick_in == 'up':
    print('moving 2nd joint in positive direction')
elif joystick_in == 'down':
    print('moving 2nd joint in the negative direction')
else:
    print('the joystick is in the neutral position, no movement')

#EXAMPLE 2
# in this example code we have a mobile robot that is equipped with proximity sensors and can detect obstacles 
# if any of the sensors detect an obstacle within a certain range, the robot should stop and display a warning message
# otherwise it should move forward

sensor1_dist = 1.5
sensor2_dist = 1.2
threshold_dist = 1

if sensor1_dist<threshold_dist or sensor2_dist<threshold_dist:
    print('warning: obstacle detected!  EMERGENCY STOPPING')
else:
    print('Marching Forward')

#EXAMPLE 3

# write a function that finds the smallest number of the three numbers
 
def min_num(a,b,c):
    if a<b and a<c:
        print('The smallest number is ' + str(a))
    elif b<a and b<c:
        print('The smallest number is '+ str(b))
    elif c<a and c<b:
        print('The smallest number is ' + str(c))
    else:
        return 'They are equal'
    
print(min_num(1,3,5))


### WHILE LOOPS ###

#is a control flow statement that allows us to repeatedly execute a block of code as long as a certain condition is true
#condition is evaluated, and if the condition is true, the code block inside the loop is executed
#if the condition evaluated is false, the loop is exited
#after the code block is run the consition is checked again
#if the condition is still true, the code block is executed again, process continues until the condition becomes false
#avoid infinite loops by giving a condition that will eventually be false
#flexible and used in various situations, particularly useful when the number of iterations is unknown or dependant on a certain condition

#EXAMPLE 1

# in this example we want to simulate a situation where a robot moves forward until it encounters an obstacle
import time
import random 

# the move_robot() function simulates the robot's movement

def move_robot(distance):
    print("Moving robot forward ...")
    # now we want to simulate the time it takes for the robot to move forward by giving some delay
    time.sleep(1)
    print(f"The robot has moved {distance} units.")
    # note that f"..." is used to create formatted string literals aka f-strings 
    # it is introduced in python 3.6 and allows you to embed expressions inside string literals


# now we should write a function for obstacle detection
def detect_obstacle():
    # simulating obstacle detection
    obstacle = random.choice([True, False])
    return obstacle 
# the random.choice() function is part of the random module in python
# it allows you to select a random element from a sequence such as a list, tuple or string 
# because we are simulating a situation here and we do not have real obstacles we randomly choose whenever an obstacle is present

# robot's initial position
position = 0

# we will keep moving the robot until an obstacle is detected
while not detect_obstacle():
    # now we should generate a random distance to move fw (because we are simulating and it's not a real scenario)
    distance = random.randint(1, 5)
    # here we call the move_robot() function to move the robot fw by the randomly generated distance 
    move_robot(distance)
    # now we will add this distance to the position of the robot
    # here we update the position of the robot
    position += distance

# here the while loop continues to execute as long as the detect_obstacle() function returns False meaning that there is no obstacle. 
# if it becomes True, then it means that there is an obstacle and the loop is exited and a message will print showing that there is an obstacle
# and the control system should take action accordingly and commands the actuators to stop the robot


print("Obstacle is detected! Stopping the robot.")
# we also print the final position of the robot
print(f"The final position of the robot is {position}")


### FOR LOOPS ###

#a control flow statement used for iterative execution
#allows us to iterate over a sequence of elements, such as list, tuple, string or any other object

# EXAMPLE #

# this is for the for loops section
# these are very basic and easy examples
# more to come in the classes and objects section

# we can use for loop with strings
# a loop that iterates over each character in the string "Robotics" and prints each character on a separate line

for letter in "Robotics":
    print(letter)

# we can also use for loops with other data types like lists
# Here we defined a list called robotics_engineers containing the names of several robotics engineers, and then we used a for loop to # iterate through each engineer's name in the list and print each name on a separate line. 

robotics_engineers = ["Tim", "Hannah", "John", "Bella"]
for robotic_engineer in robotics_engineers:
    print(robotic_engineer)

# let's do another for loop with the indexes
# Here, we are using a for loop to iterate through the indices of the robotics_engineers list, and for each index, we are printing both the # index itself and the corresponding element (name of the robotic engineer) from the list.

for index in range(len(robotics_engineers)):
    print(index)
    print(robotics_engineers[index])

# you can loop through a series of numbers or range of numbers
# The range function in Python generates a sequence of numbers starting from the first argument and ending at one less than the second argument. So the numbers generated will be from 3 to 9.
for number in range(3, 10):
    print(number)


### NESTED LOOPS ###

# a nested loop means a loop within a loop
# we can iterate through 2D lists using the nested loops
# the outer loop iterates over the rows, and the inner loop iterates over the columns
#allows us to perform operations on each element on the grid

matrix = [[1,2,3],[4,5,6],[7,8,9]]

for row in matrix:
    for element in row:
        print(element)



### CLASSES AND OBJECTS ###

#lots of other things can be represented by these data types like a person, a computer, a robot etc
#these can not be covered by the data types that we have in python
#with classes and objects we can create our own data types for anything we want
#for example a robot data type represemts a robot
#we can store all the information that we want to know about the robot inside that data type and python will create a class for it
#Classes define the blueprint or template for creating objects, and objects are instances of those classes

##CLASS -
#A user-defined blueprint or prototype that defines the attributes(data)
#and the methods(functions) that an object of that class can have
#serves as a template for creating objects
# WITH CLASS WE CAN DEFINE OUR OWN DATA TYPE

##OBJECT- 
#An object is an instance of a class
#It is created using the class template and has its own unique
#set od attributes and can perform actions defined in the class's methods

#once an object is created from the same class, it can have different attrivute values while sharing 
#the same methods defined in the class

#classes and objects allow you to organize and encapsulate data and 
#functionality in a structural manner, making the code more modular, reusable, and easier to maintain


# EXAMPLE - A simplified robot arm class that has the attributes of name, length, weight, color, and position
#to define two methods in this class
# 1- 'move' that moves the robot's position by certain angles 
# 2- 'display_info' that displays information about the robot including its new position

# this is about creating a simple robot arm class

# here the RobotArm class has the attributes of name, length, weight, and color and also position
# we use the methods move and displaye_info to rotate the robot and display the information
# the __init__ method serves as the constructor and initializes the robot arm's attributes when an object is created from the class
# the move method takes an angle parameter and updates the robot arm's position by adding the angle to the current position
# the display_info method prints the robot arm's name, length, weight, color, and current position
# here suppost that our robot arm only has one link and one joint --> 1 degree of freedom

class RobotArm:
    def __init__(self, name, length, weight, color):
        self.name = name
        self.length = length
        self.weight = weight
        self.color = color
        self.position = 0
    
    def move(self,angle):
        self.position += angle

    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Length: {self.length} cm')
        print(f'Weight: {self.weight} lbs')
        print(f'Position: {self.position} degrees')


# now let's create an object of the RobotArm class and utilize its attributes and methods

#here we create an object arm1 of the RobotArm class
#we will give the attributes Armrob, 50, 10, black
arm1 = RobotArm('Armrob',50,10,'Black')

#we call the move to update the arms position and diplay_info to display the new position and the other details
arm1.move(50)
arm1.display_info()

#we call the move and display_position again with different ones

arm2 = RobotArm('Adi', 10, 10, 'Red')
arm2.move(-15)
arm2.display_info()

#here we can import that class and all the objects can access the methods in it

from RobotArm import RobotArm

#the first RobotArm refers to the RobotArm.oy stored in the folder in a different py file, the second refers to the class name

arm3 = RobotArm('Jawa',90,-90,'Orange')
arm3.move(-90)
arm3.display_info()


### INHERITANCE ####

#Inheritance is a fundamental concept in OOP that allows classes to inherit attributes and methods from other classes
#enables code reuse, promotes modularity, and facilittes the creation of hierarchies and relationships between class
#in Py you can create a new class by deriving it from an existing class
#existing class is called the 'parent' or 'base' class, the new class is called the 'child' or the 'derived' c;ass
#child class inherits all the attributes and methods of the parent class and can also add its own unique attributes and methods
#inheritance allows the child class to reuse the code and behavious defined in the parent class while extending or modifying it to suit its specific needs
##we can have one class that has all the functionality of another class without having physically write out any of the same methods and attributes

#EXAMPLE ##

# suppose we want to create a program to simulate different types of robots
# first we will create a base class called Robot that defines common characteristics or robots
#see Robot.py

from WheeledRobot import WheeledRobot
from FlyingRobot import FlyingRobot

robot1 = WheeledRobot('Jack', 5, 6)
robot1.introduce()
robot1.move()

robot2 = FlyingRobot('Tejas',9,7)
robot2.introduce()
robot2.move()

# here you saw that the instance of WheeledRobot and FlyingRobot inherit the introduce and move methods from the Robot base class.
# they also have their own specialized implementations of the move method specific to them

# here you saw that by using inheritance we can easily extend and customize classes to represent different types of robots 
# while reusing common code from the base class

### READING FILES ###

#to read a file, we should first open it

with open('/home/jawa/Documents/INTERBOTIX PROJECT/python codes/sevsor_data.txt', 'r') as file:
    #now we iterate over each line
    for line in file:
        #split the line into timestamps and temperature
        timestamp, temperature = line.strip().split(',')

        print('Timestamp: ', timestamp)
        print('Temperature: ', temperature)

# we open the file using open() method
# the with statement makes sure that the file is properly closed after reading
# #each line is split using the split() method
# and strip() method is used to strip of any whitespaces


### MODULES AND PIP COMMAND ####


### TRY AND EXCEPT METHOD####

#in python try and except statements are used to handle exceptions
#exception is an error that occurs during the end of the program
#if exception is not handled the prog will crash
##the try block containts the code that you want to run and that might throw an exception
#the except bloclk contains the code that you want to run if an exception occurs

#EXAMPLE

def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print('Division by Zero error')
    except:
        return 'invalid'

print(divide(10,2))
print(divide(5,0))

### NUMPY ###

import numpy as np

#This is a one dimensional array 
v1 = np.array([1,2,3,4,5,6])
print(v1)

#defining another vector

v2 = np.array([7,8,9,10,11,12])

# we can do sevveral vector operations

print(v2)
print(v1+v2)

#element wise matrix multiplication
print(v1*v2)

#to know the shape of the matrix we do
print(v1.shape)

#this is a 1 row X 6 column matrix
v11 = np.array([[1],[2],[3],[4],[5],[6]])
print(v11.shape)

#we do the same with v22
v22 = np.array([[7],[8],[9],[10],[11],[12]])
print(v22.shape)

#in order to do matrix multiplication, we should multiply one by other by the transpose of the other
print(np.matmul(v11,v22.T))
print('or')
print(np.matmul(v11,np.transpose(v22))) #this will be a 6X6 matrix
print(v22.T.shape)

# @ also means matrix multiplication
print(v11.T@ v22) #which is a 1X1 vector

#to write a 2row X 6column matrix 
x = np.array([[[1],[2],[3],[4],[5],[6]],[[7],[8],[9],[10],[11],[12]]])
print(np.shape(x))

print(v1)
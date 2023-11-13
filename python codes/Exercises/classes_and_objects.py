#EXERCISE 1

class Triangle():
    def __init__(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        self.number_of_sides = 3

    def check_angles(self):
        self.sum_of_angles = self.angle1 + self.angle2 + self.angle3
        if self.sum_of_angles == 180:
            return True
        else:
            return False
        


my_triangle = Triangle(90,60,60)

print(my_triangle.number_of_sides)
print(my_triangle.check_angles())


#EXERCISE 2

class songs():
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = songs(['May god bless you', 'Happy birthday to dear appa', 'Happy birthday to you!!'])

happy_bday.sing_me_a_song()


#EXERCISE 3

class lunch():
    def __init__(self,menu):
        self.menu = menu

    def menu_price(self):
        if self.menu == 'menu1':
            print(f'Your Choice: {self.menu} price $12.00')
        elif self.menu == 'menu2':
            print(f'Your choice: {self.menu} price is $13.40')
        else:
            print('Error in Menu')

Paul = lunch('menu1')
Paul.menu_price()

#EXERCISE 4

class Point3D():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return '(%d,%d,%d)' % (self.x,self.y,self.z)
    
my_point = Point3D(1,2,3)
print(my_point)

#EXERCISE 5 (Project from Launch Code Education)

class crewCandidate():
    def __init__(self,name,mass,scores):
        self.name = name
        self.mass = mass
        self.scores = scores

    def __str__(self):
        print(f'Name: {self.name}')
        print(f'Mass: {self.mass}')
        print(f'Scores: {self.scores}')

    def add_score(self,new_score):
        self.new_score = new_score
        self.scores.append(self.new_score)

    def average(self):
        self.sum = 0
        for i in self.scores:
            self.sum += i
            self.avg = (self.sum) / len(self.scores)
        print(round(self.avg))

    def status(self):
        if self.average() == 90:
            print(f'{self.name} scored an average of {self.avg} (Accepted)')
        elif 80 <= self.average(self) <= 89:
            print(f'{self.name} scored an average of {self.avg} (Backup)')
        elif 70 <= self.average(self) <= 79:
            print(f'{self.name} scored an average of {self.avg} (Maintenence)')
        else:
            print('The robot needs to be scrapped')




candidate1 = crewCandidate('iclean',13.5,[88,85,90])
candidate1.add_score(83)
candidate1.average()
candidate1.__str__()
candidate1.status()

candidate2 = crewCandidate('Shiny',1.5,[93,88,97])
candidate2.__str__()
candidate2.average()

candidate3 = crewCandidate('DustVac',22.5,[75,78,62])
candidate3.__str__()





        




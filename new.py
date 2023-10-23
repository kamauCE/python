class students:
    def __init__(self,name,course, gender,age):
        self.name = name
        self.course = course
        self.gender = gender
        self.age = age
    def wanafunzi(self):
        print("name: %s \nCourse: %s \ngender: %s \nage: %d"
              %(self.name,self.course,self.gender,self.age))
stud1 = students("Evans Chege","ICT","Male", 22)
stud1.wanafunzi()
stud2 = students("chege kamau","computer science","male", 20)
stud2.wanafunzi()
stud3 = students("Peter","Software","male", 25)
stud4 = students("Jennie","Maths","female",24)
stud5 = students("Grace","Literature","female",23)
stud3.wanafunzi()
stud4.wanafunzi()
stud5.wanafunzi()

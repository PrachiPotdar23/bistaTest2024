class Student:
    def __init__(self,student_dictionary):
        self.student_dictionary={}
        
    def add_student(self):
        self.student_dictionary["student_name"]=input("enter your name:")
        self.student_dictionary["roll_num"]=int(input("enter your roll number:"))
        self.student_dictionary["student_class"]=input("enter your class:")
        list1=[0,1,2]
        list1[0]=input("enter your marks in english:")
        list1[1]=input("enter your marks in maths:")
        list1[2]=input("enter your marks in science:")
        self.student_dictionary["marks"]=list1
        print("student added successfully")
    
    def remove_student(self,roll_no):
        if(self.roll_num==roll_no):
            del self.roll_num
            del self.student_name
            del self.student_class
        print("student removed successfully")
            
    def update_student(self,roll_no):
        if(self.roll_num==roll_no):
            self.student_dictionary["marks"]["maths"]=input("update your marks in maths:")
            self.student_dictionary["marks"]["english"]=input("update your marks in english:")
            self.student_dictionary["marks"]["science"]=input("update your marks in science:")
            
        
        print("student updated successfully")
        
    def calculate_avg_marks(self):
        avg=self.student_dictionary["marks"]["maths"]+self.student_dictionary["marks"]["english"]+self.student_dictionary["marks"]["science"]
        
        print("Average marks of maths,english and science are: {}".format(avg))
        
    def display_student(self):
        name=self.student_dictionary["student_name"]
        roll_no=self.student_dictionary["roll_num"]
        student_class=self.student_dictionary["student_class"]
        marks=self.student_dictionary["marks"]["maths"]+self.student_dictionary["marks"]["english"]+self.student_dictionary["marks"]["science"]
        
        print(name)
        print(roll_no)
        print(student_class)
        print(marks)
        
        
stud1={}
student1=Student(stud1)
student1.add_student()
student1.display_student()
student1.calculate_avg_marks()
student1.remove_student()

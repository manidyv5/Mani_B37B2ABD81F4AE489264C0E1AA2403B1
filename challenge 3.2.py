class Student:
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa
def sort_Students(Student_list):
  sorted_Students = sorted(Student_list,key=lambda Student: Student.cgpa,reverse=True)
  return sorted_Students
Students = [
    Student("Hari", "A123", 7.8),
    Student("Abi", "A124", 8.1),
    Student("Dhinesh", "A125", 9.0),
    Student("Anu", "A126", 8.6)
]
sorted_Students = sort_Students(Students)
for Students in sorted_Students:
  print("Name: {}, Roll Number: {}, CGPA:{}".format(Student.name,Student.roll_number,Student.cgpa))
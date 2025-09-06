"""
TASK: Create an AttendanceRegister class.

Requirements:
1. The class should allow marking a student as present or absent.
2. Store attendance records in a dictionary where the student's name is the key.
3. Provide a method to check if a student was present or absent.
4. Provide a method to display the full register.

Example Usage:
    register = AttendanceRegister()
    register.mark_present("John")
    register.mark_absent("Mary")
    print(register.get_status("John"))   # "Present"
    print(register.show_register())      # {"John": "Present", "Mary": "Absent"}
"""
class AttendanceRegister:
    def __init__(self):
        self.attendance={}
    def mark_absent(self,name):
        self.attendance[name]="Absent"
        print("Student and Status successfully added")
    def mark_present(self,name):
        self.attendance[name]="Present"
        print("Student and Status successfully added")
    def get_status(self,name):
        if name in self.attendance.keys():
            return self.attendance[name]
        else:
            print("Student is not in register")
    def display_register(self):
        return self.attendance


register = AttendanceRegister()
print(register.display_register())
register.mark_present("John")
register.mark_absent("Mary")
print(register.get_status("John"))
print(register.display_register())
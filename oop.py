class Student:
    def __init__(self, name, roll, gpa):
        self.name = name
        self.roll = roll
        self.gpa = gpa

    def Welcome(self):
        print("Welcone", self.name, self.roll,)

    def get_gpa(self):
        return(self.gpa)
    
st = Student("Tamim", 20, 5.1)
st.Welcome()
print(st.get_gpa())
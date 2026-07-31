class Student:
    def __init__(self, name, branch, cgpa):
        self.name = name
        self.branch = branch
        self.cgpa = cgpa

    def approved_on_roll(self):
        if self.cgpa >= 4.5:
            return "Congratulations! You have been approved for the roll."
        return "Sorry, you have not been approved for the roll."

if __name__ =="__main__":
    try:
        name = input("Enter your name: ")
        branch = input("Enter your branch: ")
        cgpa = float(input("Enter your CGPA: "))
        check = Student(name, branch, cgpa)
        print(check.approved_on_roll())
    except ValueError:
        print("Invalid input. Please enter a valid CGPA.")
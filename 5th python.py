class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grades):
        self.students[name] = grades
        print(f"Added student '{name}' with grades {grades}.")

    def calculate_average(self, name):
        grades = self.students.get(name)
        if grades:
            avg = sum(grades) / len(grades)
            print(f"Average grade for {name}: {avg:.2f}")
        else:
            print(f"Student '{name}' not found.")

    def highest_scorer(self):
        if self.students:
            highest = max(self.students, key=lambda name: sum(self.students[name]) / len(self.students[name]))
            avg = sum(self.students[highest]) / len(self.students[highest])
            print(f"Highest scorer: {highest} with an average grade of {avg:.2f}")
        else:
            print("No students in the gradebook.")


# Main Program
if __name__ == "__main__":
    gradebook = Gradebook()

    while True:
        print("\n--- Gradebook Menu ---")
        print("1. Add Student")
        print("2. Calculate Average")
        print("3. Show Highest Scorer")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            grades = list(map(int, input("Enter grades separated by space: ").split()))
            gradebook.add_student(name, grades)
        elif choice == "2":
            name = input("Enter student name: ")
            gradebook.calculate_average(name.strip())
        elif choice == "3":
            gradebook.highest_scorer()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please try again.")

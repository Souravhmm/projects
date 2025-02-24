class StudentNode:
    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa
        self.next = None

class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, name, student_id, gpa):
        new_student = StudentNode(name, student_id, gpa)
        if not self.head:
            self.head = new_student
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_student

    def display_students(self):
        current = self.head
        if not current:
            print("No students in the list.")
            return

        print("List of Students:")
        while current:
            print(f"Name: {current.name}, ID: {current.student_id}, GPA: {current.gpa}")
            current = current.next

    def calculate_average_gpa(self):
        current = self.head
        if not current:
            print("No students in the list.")
            return 0.0

        total_gpa = 0
        count = 0
        while current:
            total_gpa += current.gpa
            count += 1
            current = current.next

        return total_gpa / count if count > 0 else 0.0

def main():
    student_list = StudentLinkedList()

    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Calculate Average GPA")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            gpa = float(input("Enter student GPA: "))
            student_list.add_student(name, student_id, gpa)
            print("Student added successfully!")
        elif choice == '2':
            student_list.display_students()
        elif choice == '3':
            average_gpa = student_list.calculate_average_gpa()
            print(f"Average GPA of students: {average_gpa:.2f}")
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
# main.py
from student_ops import add_student, view_students, update_student, delete_student
from result_ops import add_result, view_results, update_result, delete_result

def main():
    while True:
        print("\n=== Student Result Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Result")
        print("6. View Results")
        print("7. Update Result")
        print("8. Delete Result")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            add_result()
        elif choice == '6':
            view_results()
        elif choice == '7':
            update_result()
        elif choice == '8':
            delete_result()
        elif choice == '9':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
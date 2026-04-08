from grades_manager import add_student, avg_by_student

def main():
    print("Welcome to the Student Grades Manager!")
    my_grades = {}
    
    while True:
        print("\nSelect an option:")
        print("1. Add a student")
        print("2. Print student grade averages")
        print("3. Exit")
        
        choice = input()
        
        if choice == '1':
            my_grades = add_student(my_grades)
            
        elif choice == '2':
            print("\nSelect an option:")
            print("a. Display all students")
            print("b. Display selected students")
            sub_choice = input()
            
            if sub_choice == 'a':
                avg_by_student(my_grades)
            elif sub_choice == 'b':
                names_input = input("Enter student names (comma-separated): ")
                names_list = [name.strip() for name in names_input.split(',')]
                avg_by_student(my_grades, names_list)
            else:
                print("Invalid option selected!")
                
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option selected!")

if __name__ == "__main__":
    main()
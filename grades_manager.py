# Parte I: Inicializar el diccionario
def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}

def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}
    
    name_input = input("Enter student name: ")
    student_name = name_input.title()
    
    subjects = {}
    while True:
        entry = input("Enter subject and grade (or 'exit' to finish): ")
        if entry.lower() == 'exit':
            break
        
        if ',' in entry:
            subject, grade = entry.split(',')
            subjects[subject.strip().title()] = float(grade.strip())
            
    student_grades[student_name] = subjects
    print(f"Student {student_name} successfully added to the grades management system.\n")
    return student_grades
def get_students(student_grades, keys):
    subset = {}
   
    for key in keys:
        found = False
        target_name = key.title()
    
        if target_name in student_grades:
            subset[target_name] = student_grades[target_name]
            found = True
        
        if not found:
            print(f"{key.title()} not found!")
            
    return subset


def avg_by_student(student_grades, keys=None):
    
    if keys is None:
        targets = student_grades
    else:
       
        targets = get_students(student_grades, keys)
    
    for name, subjects in targets.items():
        if subjects:
            avg = sum(subjects.values()) / len(subjects)
            print(f"{name}: {avg:.1f}")
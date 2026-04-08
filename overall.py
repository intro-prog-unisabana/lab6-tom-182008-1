def student_averages(data):
    results = {}
    for student, assignments in data.items():
        grades = assignments.values()
        avg = round(sum(grades) / len(grades))
        results[student] = avg
    return results

def assignment_averages(data):
   
    first_student = list(data.keys())[0]
    assignment_names = data[first_student].keys()
    
    results = {}
    num_students = len(data)
    
    for task in assignment_names:
        total_score = 0
        for student in data:
            total_score += data[student][task]
        
        avg = round(total_score / num_students)
        results[task] = avg
        
    return results
def student_averages(data):
    if not data:
        return {}
        
    results = {}
    for student, assignments in data.items():
        grades = assignments.values()
        if not grades:
            results[student] = 0
            continue
        avg = round(sum(grades) / len(grades))
        results[student] = avg
    return results

def assignment_averages(data):
    if not data:
        return {}
    first_student = list(data.keys())[0]
    assignment_names = data[first_student].keys()
    
    results = {}
    num_students = len(data)
    
    for task in assignment_names:
        total_score = 0
        for student in data:
            # Usamos .get() con 0 por seguridad extra
            total_score += data[student].get(task, 0)
        
        avg = round(total_score / num_students)
        results[task] = avg
        
    return results
grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    formatted_stud = []
    counter = 1
    for student, grade in students.items():        
        formatted_stud.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(counter, student, grade, grades[grade]))
        counter += 1
    return formatted_stud
          

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

print (formatted_grades(students))
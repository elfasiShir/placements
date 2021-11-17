import json

def jsonify_student_data(students):
    students_list = []
    for student in students:
        student_dict = {}
        student_dict['id'] = student.id
        student_dict['first_name'] = student.first_name
        student_dict['last_name'] = student.last_name
        try:
            student_dict['roll_number'] = student.studentprofile.roll_number
        except:
            # TODO: Add a log statement here
            pass
        students_list.append(student_dict)
    return json.dumps(students_list)

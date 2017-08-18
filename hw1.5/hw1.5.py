student_group = [
        {'ID': '01','name': 'Виталий', 'surname': 'Денисов', 'sex': 'м', 'previous_experience': True, 'homework':[10, 10, 10, 10, 10], 'exam': 10},
        {'ID': '02','name': 'Игорь', 'surname': 'Денисов', 'sex': 'м', 'previous_experience': False, 'homework':[10, 10, 10, 10, 10], 'exam': 10},
        {'ID': '03','name': 'Дмитрий', 'surname': 'Тарасов', 'sex': 'м', 'previous_experience': False, 'homework':[7, 8, 7, 9, 5], 'exam': 9},
        {'ID': '04','name': 'Алексей', 'surname': 'Миранчук', 'sex': 'м', 'previous_experience': True, 'homework':[9, 10, 8, 9, 8], 'exam': 9},
        {'ID': '05','name': 'Антон', 'surname': 'Миранчук', 'sex': 'м', 'previous_experience': True, 'homework':[7, 8, 7, 6, 4], 'exam': 9},
        {'ID': '06','name': 'Дмитрий', 'surname': 'Лоськов', 'sex': 'м', 'previous_experience': True, 'homework':[9, 10, 10, 9, 9], 'exam': 9},
        {'ID': '07','name': 'Алина', 'surname': 'Кабаева', 'sex': 'ж', 'previous_experience': False, 'homework':[4, 5, 4, 3, 6], 'exam': 9},
        {'ID': '08','name': 'Тина', 'surname': 'Канделаки', 'sex': 'ж', 'previous_experience': False, 'homework':[3, 6, 7, 3, 4], 'exam': 9},
        {'ID': '09','name': 'Мальвина', 'surname': 'Кабаева', 'sex': 'ж', 'previous_experience': True, 'homework':[7, 8, 7, 9, 9], 'exam': 9}
    ]

def get_average_homework():
    homework_list = []
    homework_list = [sum(student['homework'])/len(student['homework']) for student in student_group]
    X = sum(homework_list)/len(homework_list)
    print("Среднее значение по домашним работам: ", (float('{0:.2f}'.format(X))))

get_average_homework()

def get_average_exam():
     exam_list = []
     exam_list = [student['exam'] for student in student_group]
     Y = sum(exam_list)/ len(exam_list)
     print("Среднее значение по экзамену ", (float('{0:.2f}'.format(Y))))

get_average_exam()

def get_average_homework():
    men_homework_avg = []
    women_homework_avg = []
    for student in student_group:
        if student['sex'] == 'м':
            m_homework_avg = sum(student['homework'])/len(student['homework'])
            men_homework_avg.append(m_homework_avg)
        elif student['sex'] == 'ж':
            w_homework_avg = sum(student['homework'])/len(student['homework'])
            women_homework_avg.append(w_homework_avg)
    C = sum(women_homework_avg)/len(women_homework_avg)
    A = sum(men_homework_avg)/len(men_homework_avg)
    print("Средняя оценка за домашние задания у мужчин:  ", (float('{0:.2f}'.format(A))))
    print("Средняя оценка за домашние задания у женщин:  ", (float('{0:.2f}'.format(C))))

get_average_homework()

def get_average_exam():
    men_exam_list = []
    women_exam_list = []
    for student in student_group:
        if student['sex'] == 'м':
            men_exam_list.append(student['exam'])
        elif student['sex'] == 'ж':
            women_exam_list.append(student['exam'])
    B = sum(men_exam_list)/len(men_exam_list)
    D = sum(women_exam_list)/len(women_exam_list)
    print('Средняя оценка за экзамен у мужчин: ', float('{0:.2f}'.format(B)))
    print('Средняя оценка за экзамен у женщин: ', float('{0:.2f}'.format(D)))

get_average_exam()

def get_average():
    students_with_exp = []
    students_exam_with_exp = []
    students_without_exp = []
    students_exam_without_exp = []
    for student in student_group:
        if student['previous_experience'] == True:
            avg_true_homework = sum(student['homework'])/len(student['homework'])
            students_with_exp.append(avg_true_homework)
            students_exam_with_exp.append(student['exam'])
        elif student['previous_experience'] == False:
            avg_false = sum(student['homework'])/len(student['homework'])
            students_without_exp.append(avg_false)
            students_exam_without_exp.append(student['exam'])
    E = sum(students_with_exp)/len(students_with_exp)
    F = sum(students_exam_with_exp)/len(students_exam_with_exp)
    G = sum(students_without_exp)/len(students_without_exp)
    H = sum(students_exam_without_exp)/len(students_exam_without_exp)
    print('Средняя оценка за домашние задания у студентов с опытом: ', float('{0:.2f}'.format(E)))
    print('Средняя оценка за экзамен у студентов с опытом: ', float('{0:.2f}'.format(F)))
    print('Средняя оценка за домашние задания у студентов без опыта: ', float('{0:.2f}'.format(G)))
    print('Средняя оценка за экзамен у студентов без опыта: ', float('{0:.2f}'.format(H)))
    
get_average()

def get_best_student():
    new_best_student_list = []
    for student in student_group:
        exam_grade = student['exam']
        ID = student['ID']
        avg = sum(student['homework'])/ len(student['homework'])
        Z = 0.6 * avg + 0.4 * exam_grade
        name = student['name']
        # best_student_list = ('{} {} {}'.format(ID, name, Z)).split()
        best_student_list = [ID, name, Z]
        new_best_student_list.append(best_student_list)
    b = max(new_best_student_list, key=lambda x: x[2])
    for items in new_best_student_list:
        if items[2] == b[2]:
            print('Лучший студент', 'ID: {0[0]};  Имя: {0[1]}; Балл: {0[2]}'.format(items))

get_best_student()

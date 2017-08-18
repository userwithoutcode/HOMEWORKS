student_group = [
        {'name': 'Виталий', 'surname': 'Денисов', 'sex': 'м', 'previous_experience': True, 'homework':[5, 7, 7, 8, 6], 'exam': 9},
        {'name': 'Игорь', 'surname': 'Денисов', 'sex': 'м', 'previous_experience': False, 'homework':[4, 4, 6, 8, 4], 'exam': 5},
        {'name': 'Дмитрий', 'surname': 'Тарасов', 'sex': 'м', 'previous_experience': False, 'homework':[7, 8, 7, 9, 5], 'exam': 7},
        {'name': 'Алексей', 'surname': 'Миранчук', 'sex': 'м', 'previous_experience': True, 'homework':[9, 10, 8, 9, 8], 'exam': 10},
        {'name': 'Антон', 'surname': 'Миранчук', 'sex': 'м', 'previous_experience': True, 'homework':[7, 8, 7, 6, 4], 'exam': 8},
        {'name': 'Дмитрий', 'surname': 'Лоськов', 'sex': 'м', 'previous_experience': True, 'homework':[9, 10, 10, 9, 9], 'exam': 10},
        {'name': 'Алина', 'surname': 'Кабаева', 'sex': 'ж', 'previous_experience': False, 'homework':[4, 5, 4, 3, 6], 'exam': 4},
        {'name': 'Тина', 'surname': 'Канделаки', 'sex': 'ж', 'previous_experience': False, 'homework':[3, 6, 7, 3, 4], 'exam': 5},
        {'name': 'Мальвина', 'surname': 'Кабаева', 'sex': 'ж', 'previous_experience': True, 'homework':[7, 8, 7, 9, 9], 'exam': 9}
    ]

for student in student_group:
  summa = sum(student['homework'])
  length = len(student['homework'])
  avg = summa/ length
  print(student['name'], student['surname'], avg)

homework_list = []
homework_list = [sum(student['homework'])/len(student['homework']) for student in student_group]
# print(homework_list)
summa = sum(homework_list)
lenght = len(homework_list)
X = summa/lenght
print("Среднее значение по домашним работам: ", (float('{0:.2f}'.format(X))))

exam_list = []
# for student in student_group:
exam_list = [student['exam'] for student in student_group]
summa = sum(exam_list)
length = len(exam_list)
Y = summa/ length
print("Среднее значение по экзамену ", (float('{0:.2f}'.format(Y))))

print('Средняя оценка за домашние задания у мужчин: ')
for student in student_group:
  if student['sex'] == 'м':
    A = sum(student['homework'])/len(student['homework'])
    print(A)

men_exam_list = []
for student in student_group:
  if student['sex'] == 'м':
    men_exam_list.append(student['exam'])
B = sum(men_exam_list)/len(men_exam_list)
print('Средняя оценка за экзамен у мужчин: ', float('{0:.2f}'.format(B)))

print('Средняя оценка за домашние задания у женщин: ')
for student in student_group:
  if student['sex'] == 'ж':
    C = sum(student['homework'])/len(student['homework'])
    print(C)

women_exam_list = []
for student in student_group:
  if student['sex'] == 'ж':
    women_exam_list.append(student['exam'])
D = sum(women_exam_list)/len(women_exam_list)
print('Средняя оценка за экзамен у женщин: ', float('{0:.2f}'.format(D)))

students_with_exp = []
for student in student_group:
  if student['previous_experience'] == True:
    avg = sum(student['homework'])/len(student['homework'])
    students_with_exp.append(avg)
E = sum(students_with_exp)/len(students_with_exp)
print('Средняя оценка за домашние задания у студентов с опытом: ', float('{0:.2f}'.format(E)))

students_exam_with_exp = []
for student in student_group:
  if student['previous_experience'] == True:
    students_exam_with_exp.append(avg)
F = sum(students_exam_with_exp)/len(students_exam_with_exp)
print('Средняя оценка за экзамен у студентов с опытом: ', float('{0:.2f}'.format(F)))

students_without_exp = []
for student in student_group:
  if student['previous_experience'] == False:
    avg = sum(student['homework'])/len(student['homework'])
    students_without_exp.append(avg)
G = sum(students_without_exp)/len(students_without_exp)
print('Средняя оценка за домашние задания у студентов без опыта: ', float('{0:.2f}'.format(G)))

students_exam_without_exp = []
for student in student_group:
  if student['previous_experience'] == False:
    students_exam_without_exp.append(avg)
H = sum(students_exam_without_exp)/len(students_exam_without_exp)
print('Средняя оценка за экзамен у студентов без опыта: ', float('{0:.2f}'.format(H)))

best_student_list = {}
for student in student_group:
  exam_grade = student['exam']
  summa = sum(student['homework'])
  length = len(student['homework'])
  avg = summa/ length
  Z = 0.6 * avg + 0.4 * exam_grade
  # best_student_list = {student['name']:Z for student in student_group}
  name = student['name']
  best_student_list[name] = float('{0:.2f}'.format(Z))
l = lambda x: x[1]
sorted_best_student_list = (sorted(best_student_list.items(), key=l, reverse=True))
print(sorted_best_student_list)
print(sorted_best_student_list[0])


for student in sorted_best_student_list:
  print(student[0])
  # if student[Дмитрий] in student[0]:
  #   print(student['surname'])


# print(sorted(best_student_list.items(), key=l, reverse=True))

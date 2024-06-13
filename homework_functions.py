"""from homework03-0606 import sesija, Students, Teachers, Subjects"""

"""
def insert_student(sesija, full_name, email, year, grade_macedonian, grade_math, grade_english):
    student = Students(full_name=full_name,
                    email=email,
                    year=year,
                    grade_macedonian=grade_macedonian,
                    grade_math=grade_math,
                    grade_english=grade_english)    
    sesija.add(student)
    sesija.commit()
    print(f"Studentot {full_name} e vnesen")
    return student

s1 = insert_student(sesija, "Jane", "jane@example.com", 3, 5, 5, 5)
s2 = insert_student(sesija, "Mila", "mila@example.com", 1, 5, 4, 4)
s3 = insert_student(sesija, "Jovan", "jovan@example.com", 2, 3, 3, 5)
s4 = insert_student(sesija, "Sara", "sara@example.com", 4, 5, 5, 5)
s5 = insert_student(sesija, "Viki", "viki@example.com", 3, 5, 4, 5)



def insert_teacher(sesija, full_name, email, specialty)
    teacher = Teachers(full_name=full_name,
                        email=email,
                        specialty=specialty)
    sesija.add(teacher)
    sesija.commit()
    print(f"Profesorot {full_name} e vnesen")
    return teacher

t1 = insert_teacher(sesija, "Simona", "simona@example.com", "matematika")
t2 = insert_teacher(sesija, "Viktor", "viktor@example.com", "angliski")
t3 = insert_teacher(sesija, "Kate", "kate@example.com", "makedonski")
t4 = insert_teacher(sesija, "Nikola", "nikola@example.com", "hemija")
t5 = insert_teacher(sesija, "Borjan", "borjan@example.com", "fizika")



def insert_subject(sesija, subject_name, teacher_id)
    subject = Subjects(subject_name=subject_name,
                        teacher_id=teacher_id)
    sesija.add(subject)
    sesija.commit()
    print(f"Predmetot {subject_name} e vnesen")
    return subject

sb1 = insert_subject(sesija, "matematika", 1)
sb2 = insert_subject(sesija, "angliski", 2)
sb3 = insert_subject(sesija, "makedonski", 3)
sb4 = insert_subject(sesija, "hemija", 4)
sb5 = insert_subject(sesija, "fizika", 5)
"""




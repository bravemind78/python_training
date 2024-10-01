student_scores={
    "Harry":88,
    "Ron":78,
    "Hermione":95,
    "Draco":75,
    "Nivelle":60,
}
student_grades={}
for id in student_scores:
    if 90<student_scores[id]<100:
        student_grades[id]="Outstanding"
    elif 80<student_scores[id]<=90:
        student_grades[id]="Exceeds Expectations"
    elif 70<student_scores[id]<=80:
        student_grades[id]="Acceptable"
    elif student_scores[id]<=70:
        student_grades[id]="Fail"
    else:
        student_grades[id]="Not Grading"
print(student_grades)
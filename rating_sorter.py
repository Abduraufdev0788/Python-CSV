import csv


with open('students.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    students = list(reader)

students.sort(key=lambda x : int(x['score']), reverse=True)
with open('rating.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile ,fieldnames=['rank','name','score'])
    writer.writeheader()

    i = 1
    for student in students:
        student['rank'] = i
        writer.writerow(student)
        i += 1
       
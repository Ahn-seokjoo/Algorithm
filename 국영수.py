n = int(input())
students = []
for _ in range(n):
  students.append(input().split())

students.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
#내림차순은 -를 넣어주면 된다..!!

for student in students:
  print(student[0])

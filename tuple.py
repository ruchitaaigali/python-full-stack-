student=("shree","500000","ruchi","60000")
print(student)
print(student[2])
print(student[-2])
print(student[0:2])
print(student.count(500000))



student=list(student)
student.pop()
student=tuple(student)
print(student)

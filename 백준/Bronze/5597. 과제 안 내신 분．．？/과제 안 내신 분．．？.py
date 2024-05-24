import sys
student = []
for i in range(28):
    student.append(int(sys.stdin.readline().strip()))


student.sort()
student2 = []
for i in range(1, 31):
    student2.append(i)
result = []
for i in range(30):
    if student2[i] not in student:
        result.append(student2[i])

print(result[0])
print(result[1])
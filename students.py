#!/usr/bin/env python3
n = int(input("Enter the number of students:"))
data = {} # 用来保存存储的数据的字典变量
Subjects = ('Physics', 'Maths', 'History')
for i in range(0, n):
    name = input("Enter the name of the student {}:".format(i + 1))
    marks = []
    for j in Subjects:
        marks.append(int(input("Enter marks of {} :".format(j)))) # 获得当前学生的每门学科的成绩
    data[name] = marks
for x, y in data.items():
    total = sum(y)
    print("{}'s total marks {}:".format(x, total))
    if total < 120:
        print("failed :(")
    else:
        print(x, "passed :)")

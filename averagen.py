#!/usr/bin/env python3
N = 10
sum = 0
count = 0
print("please input {} number".format(N))
while count < N:
    number = float(input())
    sum += number
    count += 1

average = sum / N
print("N = {}, Sum = {}".format(N, sum))
print("Average = {:.2f}".format(average))

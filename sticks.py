#!/usr/bin/env python3
sticks = 22

print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("Whoever will take the last stick will loose")

while True:
    print("Sticks left:", sticks)
    if sticks <= 1:
        print("You took the last stick, you loose")
        break
    sticks_taken = int(input("Take sticks(1-4):"))
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue
    if sticks - sticks_taken <= 0:
        print("You took the last stick,you loose")
        break
    computer_taken = 5 - sticks_taken
    print("Computer took:", computer_taken, "\n")
    if computer_taken >= sticks:
        print("Computer took the last stick, computer loose, your are a champion")
        break
    sticks -= 5

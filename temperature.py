#!/usr/bin/env python3
fahrenheit = 0
print("Fahrenheit Celasius")
while fahrenheit <= 250:
    celasius = (fahrenheit - 32) / 1.8
    print("{:5d} {:7.2f}".format(fahrenheit, celasius))
    fahrenheit += 25

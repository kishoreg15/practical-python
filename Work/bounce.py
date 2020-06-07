# bounce.py
#
# Exercise 1.5
height = 100
bounces = 0

while bounces < 10:
    height = height * (3/5)
    bounces += 1
    print(bounces, round(height, 4))
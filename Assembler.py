from reading_functions import *


file = open("Example.ass", "r", encoding = "utf-8")

for line in file:
    print(standarize_line(line))

file.close()
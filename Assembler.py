from validation_functions import *
from reading_functions import *


file = open("Example.ass", "r", encoding = "utf-8")
instructions = []

for line in file:
    print(standarize_line(line))
    instructions.append(standarize_line(line))

print(validate_labels(instructions))

file.close()
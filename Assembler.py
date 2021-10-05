from validation_functions import *
from reading_functions import *


readfile = input("escriba el nombre del archivo (con extension y en el mismo directorio) a revisar: \n")
start_of_CODE = 1
file = open(readfile, "r", encoding = "utf-8")
instructions = []

for line in file:
    instructions.append(standarize_line(line))


print(validate_labels(instructions,start_of_CODE))
print(logic_validation(instructions,start_of_CODE))

file.close()
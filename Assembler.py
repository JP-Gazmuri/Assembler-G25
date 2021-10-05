from validation_functions import *
from reading_functions import *


readfile = input("escriba el nombre del archivo (con extension y en el mismo directorio) a revisar: \n")
start_of_CODE = 1
file = open(readfile, "r", encoding = "utf-8")
instructions = []
validation = True

for line in file:
    if not standarize_line(line)['inlabel'] == "CODE":
        instructions.append(standarize_line(line))


if not validate_labels(instructions,start_of_CODE):
    validation = False

if not logic_validation(instructions,start_of_CODE):
    validation = False

if validation:
    print("Esta listo para ser compilado")
else:
    print("No sera compilado debido a errores")


file.close()
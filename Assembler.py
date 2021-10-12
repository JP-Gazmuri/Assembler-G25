from validation_functions import *
from reading_functions import *
from writing_functions import *


readfile = input("escriba el nombre del archivo (sin extension pero debe ser .ass y en el mismo directorio) a compilar: \n")
start_of_CODE = 1
file = open(readfile+".ass", "r", encoding = "utf-8")
instructions = []
validation = True
data = []

for line in file:
    if not standarize_line(line)['inlabel'] == "CODE":
        instructions.append(standarize_line(line))

len_code = len(instructions)
len_data = len(data)


if not full_validation(instructions,start_of_CODE):
    validation = False

if validation:
    output = full_write_file(instructions,data)
    len_out = len(output)
else:
    print("No sera compilado debido a errores")


if validation:
    outfile = open(readfile+".out","w",encoding="utf-8")
    for out in output:
        outfile.write(out)
        outfile.write("\n")
    outfile.close()


if validation:
    print(f"{len_data} lineas de datos en el archivo original")
    print(f"{len_code} lineas de codigo en el archivo original")
    print(f"{len_out} lineas de instrucciones en el archivo de salida")


file.close()
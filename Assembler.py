from validation_functions import *
from reading_functions import *
from writing_functions import *


readfile = input("escriba el nombre del archivo (sin extension pero debe ser .ass y en el mismo directorio) a compilar: \n")
file = open(readfile+".ass", "r", encoding = "utf-8")
instructions = []
data = []
start_of_CODE = 1
in_code = False
validation = True
i = 1
for line in file:
    if line.strip() == "DATA:":
        continue
    if line.strip() == "CODE:":
        in_code = True
        start_of_CODE = i+2
        continue
    if not in_code:
        variable = line.strip().split(" ")
        variable.append(i-1)
        data.append(variable)
    if in_code:
        instructions.append(standarize_line(line))
    i+=1


len_code = len(instructions)
len_data = len(data)

stack_labels(instructions)
swap_variables(instructions,data)
swap_labels(instructions)

if not full_validation(instructions,start_of_CODE,data):
    validation = False

if validation:
    output = full_write_file(instructions,data)
    len_out = len(output)
else:
    print("No sera compilado debido a errores")

if validation:
    if len(data) > 0:
        memfile = open(readfile+".mem","w",encoding="utf-8")
        for dat in data:
            memfile.write(lit_to_8bit(dat[1]))
            memfile.write("\n")
        memfile.close()
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
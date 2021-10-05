def hex_to_dec(number):
    new = number.strip("#")
    return int(new,16)

def validate_labels(instructions , start_of_CODE):
    inlabels = []
    outlabels = []
    not_inlabel = []
    i = start_of_CODE
    lenght = len(instructions)+start_of_CODE
    correct = True
    for instruction in instructions:
        if instruction['inlabel'] != "":
            inlabels.append(instruction['inlabel'])
        if instruction['outlabel'] != "":
            outlabels.append((instruction['outlabel'],i))
        i+=1
    
    for label in outlabels:
        if label[0] not in inlabels:
            not_inlabel.append(label)
            i+=1
    for outlbl in not_inlabel:
        if outlbl[0].find('#') == -1:
            try:
                position = int(outlbl[0])
                if position > lenght:
                    correct = False
                    print(f"Error en la línea numero {outlbl[1]}: La direccion {outlbl[0]} sobrepasa el largo del codigo")
            except ValueError:
                correct = False
                print(f"Error en la línea numero {outlbl[1]}: La etiqueta {outlbl[0]} no es declarada")
        else:
            position = hex_to_dec(outlbl[0])
            if position > lenght:
                correct = False
                print(f"Error en la línea numero {outlbl[1]}: La direccion {outlbl[0]} sobrepasa el largo del codigo")
    return correct


def validate_functions_syntax(lines, start_of_CODE):
    valid_functions = ["MOV","ADD","SUB","AND","OR","NOT","XOR","SHL","SHR","INC","RST","CMP","JMP","JEQ","JNE","JGT","JLT","JGE","JLE","JCR","JOV","CALL","RET","POP","PUSH"]
    correct = True
    i = start_of_CODE
    for line in lines:
        if line['function'] not in valid_functions:
            correct = False
            print(f"Error en la línea numero {i}: La funcion {line['function']} no existe.")
        i+=1
    return correct

def function_validation(line,combinations , position):
    if "AyB" in combinations:
        if line['arg1'] == "A" and line['arg2'] == "B":
            return True
        elif line['arg1'] == "B" and line['arg2'] == "A":
            return True

    if "AoByLit" in combinations:
        if  line['arg1'] == "A" or line['arg1'] == "B":
            if line['arg2'].find("#") == -1:
                try:
                    int(line['arg2'])
                    return True
                except ValueError:
                    pass
            else:
                try:
                    hex_to_dec(line['arg2'])
                    return True
                except ValueError:
                    pass

    if "AoBy(Dir)" in combinations:
        if  line['arg1'] == "A" or line['arg1'] == "B":
            dir = line['arg2'].strip("()")
            if dir.find("#") == -1:
                try:
                    int(dir)
                    return True
                except ValueError:
                    pass
            else:
                try:
                    hex_to_dec(dir)
                    return True
                except ValueError:
                    pass
    
    if "(Dir)yAoB" in combinations:
        if  line['arg2'] == "A" or line['arg2'] == "B":
            dir = line['arg1'].strip("()")
            if dir.find("#") == -1:
                try:
                    int(dir)
                    return True
                except ValueError:
                    pass
            else:
                try:
                    hex_to_dec(dir)
                    return True
                except ValueError:
                    pass
    
    if "AoBy(B)" in combinations:
        if (line['arg1'] == "A" or line['arg1'] == "B") and line['arg2'] == "(B)":
            return True

    if "(B)yA" in combinations:
        if line['arg1'] == "(B)" and line['arg2'] == "A":
            return True
    
    if "Ay(B)" in combinations:
        if line['arg1'] == "A" and line['arg2'] == "B":
            return True
    
    if "Dir" in combinations:
        if line['arg2'] == "":
            dir = line['arg1'].strip("()")
            if dir.find("#") == -1:
                try:
                    int(dir)
                    return True
                except ValueError:
                    pass
            else:
                try:
                    hex_to_dec(dir)
                    return True
                except ValueError:
                    pass
    
    if "2AoB" in combinations:
        if line['arg1'] == line['arg2'] and (line['arg1'] == "A" or line['arg1'] == "B"):
            return True

    if "(B)" in combinations:
        if line['arg1'] == "(B)" and line['arg2'] == "":
            return True
    
    if "B" in combinations:
        if line['arg1'] == "B" and line['arg2'] == "":
            return True

    if "onlyA,B" in combinations:
        if line['arg1'] == "A" and line['arg2'] == "B":
            return True
    
    if "A" in combinations:
        if (line['arg1'] == "A" or line['arg1'] == "B") and line['arg2'] == "":
            return True
    print(f"Error en linea {position}: Los argumentos no cumplen la logica para la funcion {line['function']}")
    return False

def logic_validation(lines, start_of_CODE):
    not_validated_functions = ["JMP","JEQ","JNE","JGT","JLT","JGE","JLE","JCR","JOV","CALL","RET"]
    posible_arguments = {"MOV":["AyB","AoByLit","AoBy(Dir)","(Dir)yAoB","AoBy(B)","(B)yA"],"ADD":["AyB","AoByLit","AoBy(Dir)","Ay(B)","Dir"],"SUB":["AyB","AoByLit","AoBy(Dir)","Ay(B)","Dir"],"AND":["AyB","AoByLit","AoBy(Dir)","Ay(B)","Dir"],"OR":["AyB","AoByLit","AoBy(Dir)","Ay(B)","Dir"],"NOT":["AyB","2AoB","(Dir)yAoB","(B)"],"XOR":["AyB","AoByLit","AoBy(Dir)","Ay(B)","Dir"],"SHL":["AyB","2AoB","(Dir)yAoB","(B)"],"INC":["B","Dir","(B)"],"RST":["Dir","(B)"],"CMP":["onlyA,B","AoByLit","AoBy(Dir)","Ay(B)"],"PUSH":["A"],"POP":["A"]}
    i = start_of_CODE
    answer = True
    for line in lines:
        if line['function'] != "" and line['function'] not in not_validated_functions:
            if not function_validation(line,posible_arguments[line['function']],i):
                answer = False
        i+=1
    return answer

